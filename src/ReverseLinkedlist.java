/**
 * Created by wding on 8/4/17.
 */
// 1->2-> 3 -> 4
//        ^    ^
//       head newHead
public class ReverseLinkedlist {
    private SingledLinkedlist Reverse(SingledLinkedlist head){
        if(head==null || head.next==null){
            return head;
        }

        SingledLinkedlist newHead=Reverse(head.next);
        head.next.next=head;
        head.next=null;
        return newHead;
    }

    public void Test(){
        SingledLinkedlist head=new SingledLinkedlist(1);
        head.next=new SingledLinkedlist(2);
        head.next.next=new SingledLinkedlist(3);
        head.next.next.next=new SingledLinkedlist(4);
        head.next.next.next.next=new SingledLinkedlist(5);

        SingledLinkedlist newhead = Reverse(head);
        do
        {
            System.out.print(newhead.val + "->");
            newhead = newhead.next;
        }while(newhead != null);
    }
}
