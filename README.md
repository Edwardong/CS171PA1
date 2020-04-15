#CS171 PA1
Jiaxi Ye && Zheren Dong 

##
Basic idea of how threads share information:
the main thread pushes the local and send events to the queue, the communication thread pushes the receive events, and the processing thread pops the queue and processes the events in it.
