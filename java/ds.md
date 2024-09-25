A java interface specifies a set of methods,any class that implements this interface has to provode these methods.

eaxmple 

public interface changegear(int new_value){
    geear=new_value
}

List
  - Arraylists and LinkedlIST
   A method written to work with lists will work with Arraylist and Linkedlists

    public class ListclientExample(){
        private Lits list;

        public List getlist(){
            return list;
        }

        public static void main(String[] args){
            ListclientExample ice = new ListclientExample();
            List.list = Ice.getlist();
        }
    }

    // ListclientExample does nothing useful but has esentail methods that encapsulates a List,that it it contains a List as an instance variable.

    The ListclientExample constructor initializes list by instantiating a new LinkedList,the getter method getList returns a reference to internal list object. Main tests the mthod


    Profiling - try both lists and see how long each takes 
    Constant time: An algorithm is “constant time” if the run time does not
depend on the size of the input.
Linear: An algorithm is “linear” if the run time is proportional to the
size of the input.
Quadratic: An algorithm is “quadratic” if the run time is proportional
to n2


Sort algorithm implementation swap two numebers


public class SelectionSort{

//swap i and j

public static main swapElements(int[] array, int i,int j){
    int temp = array[j];
    array[i] = array[j];
    array[j] = temp; 

}
//find index of lowest value

public static int indexLowest(int[] array, int i, int j){
    int lowIndex = start;
    for (int i = start; i< <array.length; i++>>){
        if (array[i] < array[lowIndex]){
            lowIndex =i;
        }
    }
return lowIndex;

public static void sortElemet(int[] array){
    for (int i =0; i< array.length; i++)
    {
        int j = indexLowest(array, j);
        swapElements(arry, i, j);

    }
}

}


}


A data structure is linked if its made up of objects often called nodes that contain reference to other nodes. trees and graphs contain reference to more than one other node. 

public class ListNode{
    public Object Node;
    public ListNode Next;

    public LisNode{
        this.data = Null;
        this.next = Null;

    }

    Public ListNode(Object data){
        this.data = data;
        this.next = next;
    }

    Public ListNode(object data, ListNode Next){
        this.data = data;
        this.next = nex;
    }
       
    Public String toString(){
        return "ListNode(" +data.toString() + ")"
;
    }
}

performance bug: a program that is correct in the sense that it does the right thing, but it doesn’t
belong to the order of growth we expected.

LinkedList
  order of growth 
      public class indexOf(Object target){
        Node node = head ;
        for (int i=0; i < size; i++){
            if (equals(target, node.data)){
                node = node.next;
            }
        }

        return -1;
      }

      Initially node gets a copy of head, so they both refer to the same Node. The
loop variable, i, counts from 0 to size-1. Each time through the loop, we
use equals to see if we’ve found the target. If so, we return i immediately.
Otherwise we advance to the next Node in the list.

So what is the order of growth for this method?
1. Each time through the loop we invoke equals, which is constant time (it
might depend on the size of target or data, but it doesn’t depend on
the size of the list). The other operations in the loop are also constant
time.
2. The loop might run n times, because in the worse case, we might have
to traverse the whole list.

So the run time of this method is proportional to the length of the list.


