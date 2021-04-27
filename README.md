# pyDash usando 'Dynamic Segment Size Selection' adaptado para qualidade de vídeo

Trabalho da disciplina Transmissão de Dados.

Especificações gerais do projeto [aqui](https://github.com/mfcaetano/pydash).

## gráficos obtidos para traffic_shaping=L

![playback](https://user-images.githubusercontent.com/55243078/116285057-238ddd00-a764-11eb-91c0-e99b99d008f7.png)
![playback_buffer_size](https://user-images.githubusercontent.com/55243078/116285147-3b656100-a764-11eb-8571-fe2412443716.png)
![playback_qi](https://user-images.githubusercontent.com/55243078/116285165-3e605180-a764-11eb-98eb-132e8a204ede.png)
![playback_quality_qi](https://user-images.githubusercontent.com/55243078/116285172-402a1500-a764-11eb-84e8-9b193705cb2d.png)
![throughput](https://user-images.githubusercontent.com/55243078/116285223-51732180-a764-11eb-845c-eff0990435ce.png)

### Dados gerados ao final da execução da aplicação
* Pauses number: 0
* Average QI: 17.88
  * Standard deviation: 4.4
  * Variance: 19.36
* Average QI distance: 0.26
  * Standard deviation: 1.92
  * Variance: 3.7

## gráficos obtidos para traffic_shaping=M
![playback](https://user-images.githubusercontent.com/55243078/116285253-589a2f80-a764-11eb-9ad3-ab69dc3a2177.png)
![playback_buffer_size](https://user-images.githubusercontent.com/55243078/116285266-5afc8980-a764-11eb-96d4-3d06762c9ad6.png)
![playback_qi](https://user-images.githubusercontent.com/55243078/116285296-60f26a80-a764-11eb-882c-803296b9d5c7.png)
![playback_quality_qi](https://user-images.githubusercontent.com/55243078/116285310-6485f180-a764-11eb-9ee0-d1422195efcf.png)
![throughput](https://user-images.githubusercontent.com/55243078/116285322-6780e200-a764-11eb-8b19-85f33b46dd11.png)

### Dados gerados ao final da execução da aplicação

* Pauses number: 0
* Average QI: 6.69
  * Standard deviation: 4.37
  * Variance: 19.08
* Average QI distance: 1.49
  * Standard deviation: 3.11
  * Variance: 9.66

## gráficos obtidos para traffic_shaping=H

![playback_buffer_size](https://user-images.githubusercontent.com/55243078/116285360-6e0f5980-a764-11eb-9b30-7fe971593e70.png)
![playback_pauses](https://user-images.githubusercontent.com/55243078/116285377-7071b380-a764-11eb-9174-5e2dc377ef4d.png)
![playback_qi](https://user-images.githubusercontent.com/55243078/116285394-736ca400-a764-11eb-837e-d9dd3a1f076c.png)
![playback_quality_qi](https://user-images.githubusercontent.com/55243078/116285412-76679480-a764-11eb-966e-31f4dfa0e747.png)
![throughput](https://user-images.githubusercontent.com/55243078/116285444-7a93b200-a764-11eb-918a-8be7a1879d45.png)

### Dados gerados ao final da execução da aplicação

* Pauses number: 2
  * Average Time Pauses: 1.0
  * Standard deviation: 0.0
  * Variance: 0.0
* Average QI: 0.0
  * Standard deviation: 0.08
  * Variance: 0.01
* Average QI distance: 0.0
  * Standard deviation: 0.08
  * Variance: 0.01
