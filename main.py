
import turtle



n= int(input ("Please insert a positive number"))
wn=turtle.Screen()
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    if n < 0 :
      quit ()
    count=0
    while(n != 1):
        
        if(n % 2) == 0:        # n is even
            n = n // 2
            count = count+1
        else:                 # n is odd
            n = n * 3 + 1
            count = count+1
    return(count)                  # the last print is 1

def drawGraph (n):
  """Draws a graph with positive integer on the x-axis, and the number of iterations it takes for the 3n+1 sequence to bring that integer to 1 on the y-axis. The graph marks the maximum value
  args:iteration - the upper bound, the input by user in Part A
  return:none """
  graph = turtle.Turtle()
  graph.speed(0)
  graph.up()
  graph.goto(0,0)
  graph.down()

  write= turtle.Turtle()
  write.speed(0)
  
  wn.setworldcoordinates(0,0,10,10)
  max_so_far = 0
  
  for start in range(1, n + 1): 
  

    result = seq3np1(start)
    print ("The number"+ str(start) + "has" + str(result) + "iterations.")
    
  
    for start in range (1, start + 1):
      seq3np1(start)
      print ("Start Value:", start)
      print ("Return Value:", seq3np1(start))
     
  
  
    if result > max_so_far:
      max_so_far = result
      write.clear()
      write.up()
      write.goto(start,max_so_far)
      write.write ("Maximum so far: " +str(max_so_far)) 
      wn.setworldcoordinates(0,0,start+10,max_so_far+10)
      graph.goto(start,result)
    
def main():
    
    for start in range (1,n+1):
     
      count = seq3np1 (start)
      print ("The number" + str(start) + "has" + str(count) + "iterations.")
 
  
  
drawGraph(n)
wn.exitonclick()
main()
