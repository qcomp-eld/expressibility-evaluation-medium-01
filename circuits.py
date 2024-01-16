import paddle
from paddle_quantum.ansatz import Circuit
import paddle_quantum as pq

num_qubit = 4
n_sample = 2000

class circuits_paddle:

    def circuit1(num_qubit):
        cir = Circuit(num_qubit)
        for i in range(num_qubit):
            cir.rx(i)
            cir.rz(i)

    def circuit2(num_qubit):   
        cir = Circuit(num_qubit)
        for i in range(num_qubit):
            cir.rx(i)
            cir.rz(i)
        cir.cnot([3,2])
        cir.cnot([2,1])
        cir.cnot([1,0])


    def circuit3(num_qubit):
        cir = Circuit(num_qubit)
        for i in range(num_qubit):
            cir.rx(i)
            cir.rz(i)
        cir.crz([3,2])
        cir.crz([2,1])
        cir.crz([1,0])


    def circuit4(num_qubit):
        cir = Circuit(num_qubit)  
        for i in range(num_qubit):
            cir.rx(i)
            cir.rz(i)
        cir.crx([3,2])
        cir.crx([2,1])
        cir.crx([1,0])
    

    def circuit5(num_qubit):
        cir = Circuit(num_qubit)  
        for i in range(num_qubit):
            cir.rx(i)
            cir.rz(i)

        cir.crz([3,2])
        cir.crz([3,1])
        cir.crz([3,0])

        cir.crz([2,3])
        cir.crz([2,1])
        cir.crz([2,0])

        cir.crz([1,3])
        cir.crz([1,2])
        cir.crz([1,0])

        cir.crz([0,3])
        cir.crz([0,2])
        cir.crz([0,1]) 

        for i in range(num_qubit):
            cir.rx(i)
            cir.rz(i)  


    def circuit6(num_qubit):
        cir = Circuit(num_qubit)    
        for i in range(num_qubit):
            cir.rx(i)
            cir.rz(i)

        cir.crx([3,2])
        cir.crx([3,1])
        cir.crx([3,0])

        cir.crx([2,3])
        cir.crx([2,1])
        cir.crx([2,0])

        cir.crx([1,3])
        cir.crx([1,2])
        cir.crx([1,0])

        cir.crx([0,3])
        cir.crx([0,2])
        cir.crx([0,1]) 

        for i in range(num_qubit):
            cir.rx(i)
            cir.rz(i)
    

    def circuit7(num_qubit):
        cir = Circuit(num_qubit)   
        for i in range(num_qubit):
            cir.rx(i)
            cir.rz(i)

        cir.crz([1,0])
        cir.crz([3,2])

        for i in range(num_qubit):
            cir.rx(i)
            cir.rz(i)

        cir.crz([2,1])


    def circuit8(num_qubit):
        cir = Circuit(num_qubit)      
        for i in range(num_qubit):
            cir.rx(i)
            cir.rz(i)

        cir.crx([1,0])
        cir.crx([3,2])

        for i in range(num_qubit):
            cir.rx(i)
            cir.rz(i)

        cir.crx([2,1])

    
    def circuit9(num_qubit):
        cir = Circuit(num_qubit)
        for i in range(num_qubit):
            cir.h(i)

        cir.swap([2,3])
        cir.swap([1,2])
        cir.swap([0,1])
        
        for i in range(num_qubit):
            cir.rx(i)

    
    def circuit10(num_qubit):
        cir = Circuit(num_qubit)
        for i in range(num_qubit):
            cir.ry(i)

        cir.swap([2,3])
        cir.swap([1,2])
        cir.swap([0,1])
        cir.swap([0,3])
        
        for i in range(num_qubit):
            cir.ry(i)

    
    def circuit11(num_qubit):
        cir = Circuit(num_qubit)
        for i in range(num_qubit):
            cir.ry(i)
            cir.rz(i)

        cir.cnot([3,2])
        cir.cnot([1,0])

        
        cir.ry(1)
        cir.ry(2)
        cir.rz(1)
        cir.rz(2)

        cir.cnot([2,1])
    
    
    def circuit12(num_qubit):
        cir = Circuit(num_qubit)
        for i in range(num_qubit):
            cir.ry(i)
            cir.rz(i)

        cir.swap([3,2])
        cir.swap([1,0])

        cir.ry(1)
        cir.ry(2)
        cir.rz(1)
        cir.rz(2)

        cir.swap([2,1])

    
    def circuit13(num_qubit):
        cir = Circuit(num_qubit)   
        for i in range(num_qubit):
            cir.ry(i)

        cir.crz([3,0])
        cir.crz([2,3]) 
        cir.crz([1,2])   
        cir.crz([0,1])

        for i in range(num_qubit):
            cir.ry(i)

        cir.crz([3,2])
        cir.crz([0,3]) 
        cir.crz([1,0])   
        cir.crz([2,1])
    
    
    def circuit14(num_qubit):
        cir = Circuit(num_qubit)
        for i in range(num_qubit):
            cir.ry(i)

        cir.crx([3,0])
        cir.crx([2,3]) 
        cir.crx([1,2])   
        cir.crx([0,1])

        for i in range(num_qubit):
            cir.ry(i)

        cir.crx([3,2])
        cir.crx([0,3]) 
        cir.crx([1,0])  
        cir.crx([2,1])

    
    def circuit15(num_qubit):
        cir = Circuit(num_qubit)
        for i in range(num_qubit):
            cir.ry(i)

        cir.cnot([3,0])
        cir.cnot([2,3]) 
        cir.cnot([1,2])   
        cir.cnot([0,1])

        for i in range(num_qubit):
            cir.ry(i)

        cir.cnot([3,2])
        cir.cnot([0,3]) 
        cir.cnot([1,0])   
        cir.cnot([2,1])

    
    def circuit16(num_qubit):
        cir = Circuit(num_qubit)
        for i in range(num_qubit):
            cir.rx(i)

        for i in range(num_qubit):
            cir.rz(i)

        cir.crz([1,0])
        cir.crz([3,2]) 
        cir.crz([2,1])   

    
    def circuit17(num_qubit):
        cir = Circuit(num_qubit)  
        for i in range(num_qubit):
            cir.rx(i)

        for i in range(num_qubit):
            cir.rz(i)

        cir.crx([1,0])
        cir.crx([3,2])
        cir.crx([2,1])

    
    def circuit18(num_qubit):
        cir = Circuit(num_qubit)
        for i in range(num_qubit):
            cir.rx(i)

        for i in range(num_qubit):
            cir.rz(i)

        cir.crz([3,0])
        cir.crz([2,3]) 
        cir.crz([1,2]) 
        cir.crz([0,1])

    
    def circuit19(num_qubit):
        cir = Circuit(num_qubit)
        for i in range(num_qubit):
            cir.rx(i)

        for i in range(num_qubit):
            cir.rz(i)

        cir.crx([3,0])
        cir.crx([2,3]) 
        cir.crx([1,2])  
        cir.crx([0,1]) 
