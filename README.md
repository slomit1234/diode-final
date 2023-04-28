Diode		
project

Communication protocols defense curse

Overview
1.	This project engaged in software-diodes.
2.	Focus on our own possible solution for a software diode. 
3.	 This solution handles transition of files to a network restricted area through the software diode.
Requirements
1.	Python3.10
2.	tqdm python library
(you can install using: pip insall tqdm)
Testing
1.	we simulated a true scenario (over our own home network and devices).
2.	If you don’t have a “Lab” -  You can use Docker for testing.
Links (git)
####

Our solution

1.	Our Solution consists from 4 different parts:
1.	Source-user – choose a file and send it over TCP to Proxy
2.	Proxy – acts as a buffer from all network users to the diode. Additional, we can add to it more security policies (such as file scanning, exec) to make the process as safe as possible. The Proxy transfers the data over TCP with the use in “Waterfall model”
3.	Diode – gets data only from the Proxy (otherwise, it would not continue in socket).
the diode will transfer the data to the end-user (sensitive area) using TCP.
4.	End-user – agrees to communicate with the diode only (in real life you can do it by fixing the diode IP address).

2.	High level Flowchart 
 
a.	The client sends a request to the proxy server.
b.	The proxy server receives the request and forwards it to the diode.
c.	The diode receives the request and sends it to the restricted area server.
d.	The restricted area gets the file and saves it as “received” file.
e.	Every Hop calculates the file MD5 on it’s own. (for comparing purpose).

3.	Pros & Cons comparing to the RUDP solution

Pros:

1.	TCP provides reliable and ordered delivery of data, which can be important for certain applications.
2.	TCP includes built-in mechanisms for flow control and congestion avoidance, which can help prevent network congestion and improve overall performance.
3.	TCP includes built-in error checking and retransmission mechanisms, which can help ensure the integrity of the data being transmitted.

Cons:

1.	TCP includes more overhead than UDP, which can result in slower transmission speeds and increased network traffic.
2.	TCP is more susceptible to network congestion and delays than UDP, which can negatively impact real-time applications.
3.	TCP requires more processing power and memory than UDP, which can be a concern for devices with limited resources.

4.	Diode Policies in our solution
In our implementation (works over TCP), the diode maintains its one-direction policy by using a TCP server socket to listen for incoming connections from the proxy, and a TCP client socket to connect to the proxy. The diode only accepts incoming connections from the proxy and does not actively initiate connections to the proxy. This means that data can only flow from the proxy to the diode and not the other way around, maintaining the one-direction policy of the diode.
 
5.	Waterfall model
the data transfer from the proxy to the diode using TCP follows a Waterfall model, in the sense that the data is pushed downstream in a one-way flow without any feedback or acknowledgement from the receiver. In this implementation, the proxy sends the data to the diode using the send() method of the socket object. The diode then receives the data using the recv() method of the client socket object, and the received data is stored in the buffer. There is no feedback or acknowledgement sent back to the proxy, which makes this a one-way data transfer in a Waterfall model.

Getting Started

source user
The process always starts with a need, in our case passing files to the organization restricted area.

For generating a file, we have created “generate.py”. this short script will create you a file in every name or size
 
 

Now, let’s talk about the user itself.
The user connects to the Proxy and starts to send the file in chunks to the proxy over TCP (as requested).

The user also has a progress bar that can be compare to the end-user progress bar to see the delay in the network.

Testing – 
You can see your own ip address using ipconfig
 
Than use “python generate.py” to generate file to send to the end-user
 
 
Than run “python src-user.py”
 

proxy
The proxy’s purpose is to be like a “middleman” between the “insecure network” to the diode.

It minimizes the attack surface, because then the diode's IP address and network information are hidden from the users. This means that the diode is only can put all of her security efforts between her and the proxy. This makes it harder for an attacker to directly target the end-user.

Enables additional security policies. The proxy can have control of everything that’s going to the diode.
it can be used to add more security policies such as file scanning, encryption, authentication feature and more..

Allows monitoring. It will become easier to monitor and audit the traffic going to diode from the src-user.
Our proxy is very minimal and just passing the information to the diode using TCP sockets.

By comparing all the MD5 from all devices you can see that the HASH stayed the same.

Testing – 
The proxy ipconfig (for src-user.py)
 
run “python proxy.py”
 
diode
The implementation of the diode ensures a one-directional data flow by opening a TCP socket and listening for incoming data from the proxy on a specific port. When data is received, it is processed and then forwarded to the end-user over a separate TCP connection. However, there is no communication back to the proxy over the same connection, so the data flow is one-directional.

Testing –
Network configuration (for proxy.py)
 
run “python diode.py”
 
end user
the end user is the target!
it has a progress bar to follow the file transmission.
The end-user will create a “received.txt” when done receiving the whole file data.
 
The end-user will only receive data from diode.

Testing – 
 
run “python end-user.py”
 
Notes for Testing
The right order to run all files:
1.	Python end-user.py
2.	Python diode.py
3.	Python proxy.py
4.	Python src-user.py

Remember also to change the addresses and ports according the ipconfig command

You might need to turn off your firewall settings for this to work.
