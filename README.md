# CS171 PA1

Jiaxi Ye && Zheren Dong 

## Basic idea of how threads share information:
The main thread pushes the local and send events to the queue, the communication thread pushes the receive events, and the processing thread pops the queue and processes the events in it.
(have the main thread loop on user input, one to wait on a socket (communication thread), and one to process any event (processing thread))


Sample message:  
3receiveP1P2LetsDance


Launch process:

`$python3 process.py <pid=1|2|3>`


Input format:

- `print`

- `local <event>` 
    
  e.g. `local abcdef`

- `send P<pid> <event>` 

  e.g. `send P1 qwerty`

