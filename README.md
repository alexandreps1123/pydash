# pyDash usando 'Dynamic Segment Size Selection' adaptado para qualidade de vídeo

Trabalho da disciplina Transmissão de Dados.

Especificações gerais do projeto [aqui](https://github.com/mfcaetano/pydash).

## gráficos obtidos para traffic_shaping=L

#### playback

![playback](https://user-images.githubusercontent.com/55243078/116580124-73e27780-a8e9-11eb-9ae4-39d9b28f2bc5.png)

#### playback_buffer_size

![playback_buffer_size](https://user-images.githubusercontent.com/55243078/116580139-7775fe80-a8e9-11eb-98ef-966e7625567c.png)

#### playback_qi

![playback_qi](https://user-images.githubusercontent.com/55243078/116580160-7a70ef00-a8e9-11eb-8ce9-ca7c8f83c31d.png)

#### playback_quality_qi

![playback_quality_qi](https://user-images.githubusercontent.com/55243078/116580171-7d6bdf80-a8e9-11eb-8fcf-3719652dfb98.png)

#### throughput

![throughput](https://user-images.githubusercontent.com/55243078/116580179-7f35a300-a8e9-11eb-91d3-05e6f8f52ef5.png)

### Dados gerados ao final da execução da aplicação
* Pauses number: 0
* Average QI: 16.95
  * Standard deviation: 5.52
  * Variance: 30.43
* Average QI distance: 0.16
  * Standard deviation: 1.42
  * Variance: 2.01

## gráficos obtidos para traffic_shaping=M

#### playback

![playback](https://user-images.githubusercontent.com/55243078/116580582-e2273a00-a8e9-11eb-936f-6cd73ca98abd.png)

#### playback_buffer_size

![playback_buffer_size](https://user-images.githubusercontent.com/55243078/116580655-f0755600-a8e9-11eb-818b-8fee3e445192.png)

#### playback_qi

![playback_qi](https://user-images.githubusercontent.com/55243078/116580674-f53a0a00-a8e9-11eb-97ca-0e6e7448b15b.png)

#### playback_quality_qi

![playback_quality_qi](https://user-images.githubusercontent.com/55243078/116580685-f9662780-a8e9-11eb-9ac0-96d89b1cf1c7.png)

#### throughput

![throughput](https://user-images.githubusercontent.com/55243078/116580698-fe2adb80-a8e9-11eb-9b3a-341e41ed82f3.png)


### Dados gerados ao final da execução da aplicação
* Pauses number: 0
* Average QI: 6.68
  * Standard deviation: 4.35
  * Variance: 18.95
* Average QI distance: 1.14
  * Standard deviation: 2.66
  * Variance: 7.06

## gráficos obtidos para traffic_shaping=H

#### playback

![playback](https://user-images.githubusercontent.com/55243078/116582027-50b8c780-a8eb-11eb-857d-f580210860c8.png)

#### playback_buffer_size

![playback_buffer_size](https://user-images.githubusercontent.com/55243078/116582040-531b2180-a8eb-11eb-9cb7-e6b58f1520be.png)

#### playback_pauses

![playback_pauses](https://user-images.githubusercontent.com/55243078/116582119-65955b00-a8eb-11eb-93b5-2f548a950231.png)

#### playback_qi

![playback_qi](https://user-images.githubusercontent.com/55243078/116582140-6d54ff80-a8eb-11eb-92fc-05ef1d3f46cb.png)

#### playback_quality_qi

![playback_quality_qi](https://user-images.githubusercontent.com/55243078/116582158-73e37700-a8eb-11eb-9825-4d20f3b9f3d5.png)

#### throughput

![throughput](https://user-images.githubusercontent.com/55243078/116582194-7cd44880-a8eb-11eb-8a74-b4b34b5984dd.png)

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
