function addinputFields(){
    var number = document.getElementById("sub").value;
    for (i=1;i<number;i++){
        var elem = document.querySelector('#clone'+i);
        var clone = elem.cloneNode(true);
        clone.id = 'clone'+(i+1);
        elem.after(clone);
    }
    // document.getElementById(count).style.display = 'none';
    
}
