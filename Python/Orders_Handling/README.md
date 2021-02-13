# Quickstart

This project is based on Python 3 (v3.6) and tested on Mac Pro laptop.

To run the program
* unpack the files into a folder
* in a terminal, cd into the folder 
* run "python main.py -h", it will show command line options
* for example, "python main.py -of orders.json"
* or to change to 4 orders per 1 sec, "python main.py -of orders.json -op 4"
* or to change to 1 order per 2 sec, "python main.py -of orders.json -op 0.5"

# Console Messages
* prefex ">" means a new order placed on a shelf, followed by the entire content of each shelf after the event
  * e.g.,  > shelf frozen has a new order id:a8cfcb76-7f24-4420-a5ba-d46dd77bdffd, name:Banana Split, temp:frozen, shelfLife:20, decayRate:0.63, value:1.00
* prefix "<" means an order is picked up by pickup thread, followed by the entire content of each shelf after the event
  * e.g., < picked up order id:a8cfcb76-7f24-4420-a5ba-d46dd77bdffd, name:Banana Split, temp:frozen, shelfLife:20, decayRate:0.63, value:0.91 from shelf frozen
* prefix "<>" means a selected order is moved from overflow shelf to its own temperature shelf because overflow shelf reached capacity
* no prefix message indicates some critical events -- capacity overflow, overflow order re-arrange, dispose order as waste, etc.

# Design & Development
* Overall design
  * There are 4 types of threads -- 1 main thread creates 1 order_processing thread, 1 cleanup thread and n pickup_processing threads
  * Shelves - normal temperature shelves and 1 overflow shelf, each shelf will have its own thread Lock
  * overflow handling
      * for a given order, if the desired temperate shelf is at capacity, check overflow shelf
      * if overflow shelf is at capacity, then loop through all order in overflow shelf and find out if there are available capacity for any order, then there 2 cases
      * 1st case is that no other shelves have capacity, then randomly dispose an order as waste from overflow shelf, and add the order to overflow shelf  
      * 2nd case is that if a shelf (A) is available, we want to move the order from overflow shelf to shelf A, here we choose first add the order to Shelf A, then remove it from overflow shelf
      * in race condition, because shelf's thread lock is for its own shelf, during the above move, this order could be picked up from overflow shelf (by the pickup thread) before being removed from overflow shelf, which results in an orphan order in shelf A
      * the solution is to check order state, and to mark order state picked_up after the order is picked up, so the orphan order will be cleaned up from the shelf based on this state
  * order state
      * there are 3 states for each order - received, picked up, wasted
  * cleanup thread
      * The purpose of this thread is to loop through all shelves to remove 2 kinds of orders
        (1) orders with 0 value, (2) orphan orders with picked_up = True
      * without cleanup thread, an order with 0 value could stay on the shelf until pickup, which occupies shelf space.
        Clean up thread could improve shelf's efficiency by timely removing orders with 0 value to increase capacity
  * pickup_queue
      * after order is received, the order will be put into pickup_queue
      * pick up thread will process the queue in FIFO manner to pick up the order
      * order can only be picked up randomly between 2 - 6 seconds after received
  * For pickup_thread and cleanup_thread, the thread delay time can be changed in the file

# Unit Test
* Quick Test (by setting up virtualenv)
  * ./tests/test.sh


