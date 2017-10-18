/**
 * Created by MSI GP72 on 10/18/2017.
 */
public class simulator {


    public static void main(String args[]){
        stateStruct state;

    }

    public void printState(stateStruct s){
        int i;
        System.out.printf("\n@@@\nstate:\n");
        System.out.printf("\tpc %d\n", s.pc);
        System.out.printf("\tmemory:\n");
        for (i=0; i< s.numMemory; i++) {
            System.out.printf("\t\tmem[ %d ] %d\n", i, s.mem[i]);
        }
        System.out.printf("\tregisters:\n");
        for (i=0; i < 8 ; i++) {
            System.out.printf("\t\treg[ %d ] %d\n", i, s.reg[i]);
        }
        System.out.printf("end state\n");
    }
}
