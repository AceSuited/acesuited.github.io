---
title:  "로드밸런싱이란 (loadbalancing)"
layout: single
categories: 
  - network

tags:
  - [CS, network]

toc: true
toc_sticky: true

date: 2022-03-18
last_modified_at: 2022-03-18
---
# Load Balancing

# 로드밸런싱이란?

로드 밸런싱은 네트워크 또는 서버에 가해지는 부하(=로드) 를 분산(=벨런싱)해주는 기술을 의미한다. 로드밸런싱 기술을 제공하는 서비스 또는 장치(로드밸런서)는 클라이언트와 네트워크 트래픽이 집중되는 서버들 또는 네트워크 허브 사이에 위치한다.

특정 서버 또는 네트워크 허브에 부하가 집중되지 않도록 트래픽을 다양한 방법으로 분산하여 서버나 네트워크 허브들의 성능을 최적인 상태로 유지할 수 있도록 한다.

# 로드밸런서의 기본 동작 방식

1. 클라이언트의 브라우저에서 naver.com을 요청
2. 클라이언트 브라우저에 설정된 메인 DNS 서버로 naver.com의 IP 주소를 질의(DNS query)
3. 메인 DNS 서버는 [naver.com](http://naver.com) 주소를 관리하는 별도의 DNS 서버에 IP 주소 query
4. 별도 관리 DNS 서버는 naver.com의 로드밸런서의 IP(Virtual IP) 주소를 메인 DNS 서버에게 전달.
5. 메인 DNS 서버는 획득한 VIP 주소를 클라이언트에게 전송(DNS Response)
6. 클라이언트에서 로드밸런서의 VIP 주소로 http 요청
7. 로드 밸런서는 별도 로드밸런싱 방법( 라운드 로빈 등) 을 통하여 서버에게 요청을 전송
8. 서버의 작업 결과를 받은 로드밸런서는 전달받은 http 결과를 클라이어언트에게 전송

# 로드밸런서의 기본 기능

1. Health Check

기본적으로 보통의 로드밸런서는 서버들(또는 다음의 노드) 에 대한 주기적인 Health Check를 통해 서버들의 장애 여부를 판단할 수 있다. 이로 인해 로드밸런서가 있을 때 서버 몇 대에 이상이 생기더라도 다른 정상 동작중인 서버로 트래픽을 보내주는 Fail-Over 가 가능하며, 더불어 TCP/UDP 분석이 가능하기 때문에 Firewall의 역할도 수행할 수 있다.

- L3 check : ICMP를 이용하여 서버의 IP 주소가 통신 가능한 상태인지를 확인한다.
- L4 check : TCP의 3-way handshaking 을 이용하여 각 포트 상태를 체크한다. 예를 들어 HTTP 웹 서버의 경우 80포트를 사용하므로 TCP 80 포트에 대한 3-wat hanshake 체크를 통해 서버가 살아있는 상태인지를 확인한다.
- L7 체크 : 어플리케이션 계층에서 체크를 한다. 즉 실제 웹 페이지(ex .../index.html)에 통신을 시도하여 이상 유무를 파악한다.

1. Tunneling

눈에 보이지 않는 가상의 통로를 만들어 통신할 수 있게 하는 개념으로 로드밸런서는 클라이언트와 서버 간 중간에서 터널링을 제공해준다. 즉 연결된 상호간에만 캡슐화된 패킷을 구별해 캡슐화를 해제하게 한다.

1. NAT(Network Address Translation)

IP 주소를 변환해주는 기능이다. 하나의 공인 IP로 여러 개의 사설 IP 공간을 은닉하는 IP masquerading 기법을 사용한다. 다수의 통신기기가 하나의 공인 IP를 사용하여 외부 인터넷을 사용하는 것을 가능하게 해준다.

로드밸런싱 관점에서는 여러개의 호스트가 하나의 공인 IP 주소를 통해 접속하게 하는 것이 주 목적이다.

- SNAT( Source Network Address Translation)
    
    내부에서 외부로 트래픽이 나가는 경우, 내부 사설 IP 주소를 외부의 공인 IP 주소로 변환하는 방식이다. 집에서 사용하는 공유기가 대표적인 예이다.
    
- DNAT( Destination Network Address Translation)
    
    외부에서 내부로 트래픽이 들어오는 경우, 외부 공인 IP 주소를 내부의 사설 IP 주소로 변환하는 방식이다. 로드밸런서가 대표적인 예이다.
    
1. DSR( Direct Server Routing)

서버에서 클라이언트로 되돌아가는 경우, 목적지를 클라이언트로 설정한 다음 네트워크 장비나 로드밸런서를 거치지 않고 바로 클라이언트를 찾아가는 방식이다 이 경우, 로드밸런서의 부하를 줄여줄 수 있는 장점이 있다.

<br>

<img width="686" alt="image" src="https://user-images.githubusercontent.com/61482670/158862698-1244b49f-9b01-440d-8775-4c659d7bdce7.png">

<br>

# 로드밸런싱 종류와 방법(L4, L7계층)

1. L4 로드밸런싱

L4 로드 밸런서는 네트워크 계층(IP) 과 트랜스포트 계층(TCP,UDP) 의 정보를 바탕으로 로드를 분산한다,

즉 IP 주소나 포트번호 MAC 주소, 전송 프로토콜 등에 따라 트래픽을 나누고 분산처리하는 것이 가능하다. 이런 이유로 L4 로드밸런서를 CLB(Connection Load Balancer) 혹은  SLB(Session Load Balancer)라고 부르기도 한다. 

L4 로드밸런싱에는 다음과 같은 방법들이 있다.

- 라운드 로빈(Round Robin) : 세션을 각 서버에 순차적으로 맺어주는 방식. 단순히 순서에 따라 세션을 할당하므로 경우에 따라 경로별 균등한 처리량을 보장할 수 없다.
- 가중치 및 비율 할당 방식 : 서버마다 비율을 설정해 두고 해당 비율 만큼 세션을 맺어주는 방식. 예를 들어 특정 서버의 성능이 월등히 뛰어나다면 해당 서버로 세션을 많이 맺어주도록 가중치를 설정하고 나머지 로우급들의 서버들은 적은 세션이 맺어질 수 있도록 가중치를 설정한다.
- 최소연결(Least Connection)기반 : 가장 적은 세션을 가진 서버로 트래픽을 보내는 방식이다.(가장 많이 사용되는 방법)
- 응답 시간 기반: 가장 빠른 응답 시간을 보내는 서버로 트래픽을 밸런싱해주는 방식이다. 예를 들어 각 서버들의 가용한 리소스와 성능, 그리고 처리중인 데이터 양 등이 다를 경우 적합한 방식이다.
- 해시 기반: 특정 클라이언트는 특정 서버로만 할당시키는 방식이다. 예를 들어, 특정 IP 주소 혹은 포트의 클라이언트들은 특정 서버로만 세션이 맺어지도록 한다. 경로가 보장되며 접속자 수가 많을수록 분산 및 효율이 뛰어난다.
- 대역폭 기반: 서버들과의 대역폭을 고려하여 트래픽을 분산하는 방식이다.

1. L7 로드밸런싱

L7 로드 밸런서는 위와 같은 L4 로드밸런서의 기능을 포함하는 것 뿐 만 아니라 OSI 7계층의 프로토콜(ex. http smtp, ftp 등) 을 바탕으로도 분산 처리가 가능하다. 예를 들어, 온라인 쇼핑몰의 장바구니에 물건들을 담아놓았는데 다른 서버에서의 처리는 어려울 것이다. L7 로드밸런싱에는 다음과 같은 방법들이 있다.

- URL 스위칭 : 특정 하위 URL 들은 특정 서버로 처리하는 방식이다. 예를들어 ‘../abc/image'  또는 ‘../abc/video’ 와 같은 특정 URL을 가진 주소들은 서버가 아닌 별도의 스토리지에 있는 객체 데이터로 바로 연결되도록 구성할 수 있다.
- 컨텍스트 스위칭 : 클라이언트가 요청한 특정 리소스에 대해 특정 서버 등으로 연결할 수 있다. 예를 들어 이미지 파일에 대해서는 확장자를 참조하여 별도로 구성된 이미지 파일이 있는 서버/스토리지로 직접 연결해줄 수 있다.
- 쿠키 지속성 : 쿠키 정보를 바탕으로 클라이언트가 연결 했었던 동일한 서버에 계속 할당해주는 방식이다. 특히 사설 네트워크에 있던 클라이언트의 IP 주소가 공인 IP 주소로 치환되어 전송(X-Forwarded-For 헤더에 클라이언트 IP 주소를 별도 기록) 하는 방식을 지원한다.
    - `X-Forwarded-For`
        - HTTP 또는 HTTPS 로드 밸런서를 사용할 때 클라이언트의 IP 주소를 식별하는 데 도움을 줍니다.
    - `X-Forwarded-Proto`
        - 클라이언트가 로드 밸런서 연결에 사용한 프로토콜(HTTP 또는 HTTPS)을 식별하는 데 도움을 줍니다.
    - `X-Forwarded-Port`
        - 클라이언트가 로드 밸런서 연결에 사용한 포트를 식별하는 데 도움을 줍니다.

<img width="707" alt="image" src="https://user-images.githubusercontent.com/61482670/158862920-bce57a77-8101-4af5-8d86-b3b160cdd66b.png">

<BR>

# L4밸런서와 L7밸런서 비교

<img width="691" alt="image" src="https://user-images.githubusercontent.com/61482670/158863146-79618c96-f879-4e2e-89ec-b146feabd676.png">

<br>

# 추가로 고려할 점

<BR>

💡 로드밸런서 또한 완벽한 장비가 아니므로 장애가 날 경우를 대비하여 로드밸런서 자체도 이중화 구성을 할 필요가 있다.


<BR>


# Reference

[https://www.stevenjlee.net/2020/06/30/이해하기-네트워크의-부하분산-로드밸런싱-load-balancing-그/](https://www.stevenjlee.net/2020/06/30/%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EC%9D%98-%EB%B6%80%ED%95%98%EB%B6%84%EC%82%B0-%EB%A1%9C%EB%93%9C%EB%B0%B8%EB%9F%B0%EC%8B%B1-load-balancing-%EA%B7%B8/)

[https://brunch.co.kr/@sangjinkang/61](https://brunch.co.kr/@sangjinkang/61)

[https://tecoble.techcourse.co.kr/post/2021-11-07-load-balancing/](https://tecoble.techcourse.co.kr/post/2021-11-07-load-balancing/)

[https://nesoy.github.io/articles/2018-06/Load-Balancer](https://nesoy.github.io/articles/2018-06/Load-Balancer)