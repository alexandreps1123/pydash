# -*- coding: utf-8 -*-

from r2a.ir2a import IR2A
from player.parser import *
from base.whiteboard import Whiteboard
import time
import statistics


class R2ADynamicSegmentSizeSelection(IR2A):

    def __init__(self, id):
        IR2A.__init__(self, id)
        self.whiteboard = Whiteboard.get_instance()

        self.parsed_mpd = ''
        self.qi = []
        self.throughputs = []

        # q1[1] = 91917bps
        self.selected_qi = [91917]
        self.request_time = 0.0


    # quando 'request' tem que enviar a 'mensagem' pra baixo 'send_down(msg)'
    def handle_xml_request(self, msg):
        self.request_time = time.perf_counter()

        self.send_down(msg)

    # quando 'response' tem que enviar a 'mensagem' pra cima 'send_up(msg)'
    def handle_xml_response(self, msg):
        # getting qi list
        self.parsed_mpd = parse_mpd(msg.get_payload())
        self.qi = self.parsed_mpd.get_qi()

        rtt = time.perf_counter() - self.request_time
        throughput = msg.get_bit_length()/(rtt/2.0)
        self.throughputs.append(throughput)

        #--------------enviar o segmento para o player

        self.send_up(msg)

    # define a qualidade do segmento que vai ser pedido
    def handle_segment_size_request(self, msg):
        self.request_time = time.perf_counter()

        #--------fazer o calculo da qualidade a ser pedida-------------
     
        # calcula a media simples do historico de vazao
        media = statistics.mean(self.throughputs)

        # calculo do sigma^2
        # somatorio de i = 1 ate m de (i/m)*|self.throughputs - media|
        # m eh o numero de vazoes medidas
        # i eh o peso de cada vazao, a ultima vazao medida tem maior peso
        sigma_quadrado = 0.0
        m = len(self.throughputs)
        for i, data in enumerate(self.throughputs):
            sigma_quadrado += ((i+1)/m)*abs(data - media)
            
        # p pertence ao intervalo [0,1]
        # p eh usado para estimar a possibilidade de aumentar ou diminuir a qualidade do video
        p = media/(media+sigma_quadrado)
        
        # pegar a posicao da ultima qualidade selecionada dentro da lista de qualidades possiveis
        last_qi = 0
        for i in range(len(self.qi)):
            if self.qi[i] == self.selected_qi[len(self.selected_qi) -1]:
                last_qi = i
                
        # tau eh a 'disposicao' para diminuir a qualidade do video
        # tau = (1 - p)*omega[max(0, last_qi - 1)]
        # em que omega eh uma lista de tamanho N com todas as qualidades possíveis
        tau = (1 - p)*max(0, self.qi[last_qi-1])

        # teta eh a 'disposicao' para aumentar a qualidade do video
        # teta = p*omega[min(N, last_qi + 1)]
        teta = p*min(self.qi[19], self.qi[last_qi+1])

        # new_qi = argmin(omega[i] - tau + teta)
        # ======================> NOTA
        # ate o momento esta sendo pego os resultados positivos
        # entre (omega[i] - tau + teta)
        # ainda eh preciso verificar se esta eh a melhor abordagem
        new_qi = []
        for i in self.qi:
            if (i - tau + teta) > 0:
                new_qi.append(i - tau + teta)
        
        # 
        for i in self.qi:
            if min(new_qi) > i:
                self.selected_qi.append(i)

        print('========================>')
        playback_qi = self.whiteboard.get_playback_qi()
        buffer_size = self.whiteboard.get_playback_buffer_size()
        # time_playback = self.whiteboard.get_playback_segment_size_time_at_buffer()
        if len(buffer_size) > 0:
            print('buffer size = '+str(buffer_size[len(buffer_size)-1][1]))
        if len(playback_qi) > 0:
            print(' video QI = '+str(playback_qi))
        print(self.selected_qi[len(self.selected_qi) - 1])
        print('========================')
        print('========================')

        # adiciona a msg a qualidade a ser pedida
        msg.add_quality_id(self.selected_qi[len(self.selected_qi) - 1])

        # envia o pedido do segmento de qualidade definida para o servidor
        self.send_down(msg)

    # quando o 'response' chega tem-se que calcular a qualidade do proximo segmento (?)
    def handle_segment_size_response(self, msg):
        rtt = time.perf_counter() - self.request_time        
        throughput = msg.get_bit_length()/(rtt/2.0)
        self.throughputs.append(throughput)

        self.send_up(msg)

    def initialize(self):
        pass

    def finalization(self):
        pass
