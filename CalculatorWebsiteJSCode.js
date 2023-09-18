function add(){
    var numberOne,numberTwo,sum;
    numberOne=Number(document.getElementById("first").value);
    numberTwo=Number(document.getElementById("second").value);
    sum = numberOne + numberTwo;
    document.getElementById("answer").value = sum;
    }