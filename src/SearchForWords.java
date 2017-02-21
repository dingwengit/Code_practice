import java.util.ArrayList;

/**
 * Created by wding on 2/20/17.
 */
public class SearchForWords {

    /*
    Question : given the matrix below, start from any point to traverse each element once,
    add all characters of the path to form a string, if the string is in a predefined dictionary,
    print out the word.
    */
    private final char[][] _matrix = {
            {'c','a','t','s'},
            {'o','o','k','t'},
            {'a','i','a','e'},
            {'k','o','k','a'}
    };

    private class Item{
        public Item(int i, int j){row=i;col=j;}
        public String getString(){return str;}
        public void setString(String s) {str=s;}
        private int row;
        private int col;
        String str;

        @Override
        public boolean equals(Object obj) {
            Item other = (Item)obj;
            return this.col == other.col && this.row == other.row;
        }
    }
    private ArrayList<String> _dictionary = new ArrayList<String>();

    private void SearchForWords(char[][] m){
        ArrayList<Item> t = new ArrayList<Item>();
        for(int i=0;i < m.length; i++){
            for(int j=0; j<m[0].length;j++){
                t.clear();
                Item item = new Item(i, j);
                item.setString(String.valueOf(m[i][j]));
                t.add(item);
                PrintWords(m, i, j, t);
            }
        }
    }

    private void CheckWord(String str){
        if(_dictionary.contains(str)){
            System.out.println(str);
        }
    }

    private boolean Traverse(char[][] m, int r, int c, ArrayList<Item> t){
        if(r>=0 && r< m.length && c>=0 && c < m[0].length){
            Item item = new Item(r, c);
            if(t.contains(item) == false){
                item.setString(((Item)t.get(t.size()-1)).getString() + String.valueOf(m[r][c]));
                t.add(item);
                return true;
            }
        }
        return false;
    }

    private void  PrintWords(char[][] m, int r, int c, ArrayList<Item> t){
        // check if current string is a valid word and print
        CheckWord(((Item)t.get(t.size()-1)).getString());
        // go right
        if(Traverse(m, r, c+1, t)){
            PrintWords(m, r, c+1, t);
        }
        // go down
        if(Traverse(m, r+1, c, t)){
            PrintWords(m, r+1, c, t);
        }
        // go left
        if(Traverse(m, r, c-1, t)){
            PrintWords(m, r, c-1, t);
        }
        // go up
        if(Traverse(m, r-1, c, t)){
            PrintWords(m, r-1, c, t);
        }
        // remove the last item
        t.remove(t.size()-1);
    }

    public void test(){
        _dictionary.add("cook");
        _dictionary.add("cat");
        _dictionary.add("cats");
        _dictionary.add("tea");
        _dictionary.add("stac");

        SearchForWords(_matrix);

    }
}
