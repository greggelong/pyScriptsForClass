
IntList fibo;
float x=0;
float y=0;
float sz =1;
float ang = HALF_PI;
float phi = 1.61803;
// using the aproximation of phi by dividing fibonacci numbers
void setup(){
  size(987,610);
  background(0);
  //rectMode(CENTER);
  noFill();
  stroke(255,255,0);
  strokeWeight(3);
  fibo = new IntList();
  fibo.append(1);
  for (int i =1; i<16;i++){
    println(fib(i));
    fibo.append(fib(i));
  } 
  fibo.sortReverse();
  println(fibo);
  
  wreck();
}

void wreck(){
  translate(0,0);
  rotate(radians(-90)); // need to rotate opposite dir to set up correctly for first rotation
  for (int i =0; i<fibo.size()-1;i++){
    translate(x,0);
    rotate(radians(90)); // rotate
    // width of square
    float w = fibo.get(i)*sz;
    fill(random(255),random(255),random(255));
    square(0,0,w);
    arc(w,w,2*w,2*w,PI,PI+HALF_PI);
    //x=w*phi; // using the aprox of phi 
    // need to recast as a float
    float myphi = fibo.get(i)/float(fibo.get(i+1));
    println(fibo.get(i),fibo.get(i+1),myphi);
    x=w*myphi;
  
  }
}


int fib(int n){
    if(n <=2){
        return 1;
    }
    else{
        int f1 =1;
        int f2 =1;
        int result = 0;
        for(int i =3; i<n+1; i++){
            result = f1 + f2;
            f1= f2;
            f2 = result;
        }
    return result;
    }
}
