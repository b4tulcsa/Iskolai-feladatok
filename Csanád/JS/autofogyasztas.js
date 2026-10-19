function muvelet(){
            const oraallas1 = parseInt(document.getElementById("adat1").value);
            const oraallas2 = parseInt(document.getElementById("adat2").value);
            const mennyi = parseInt(document.getElementById("adat3").value);
            const ar = parseInt(document.getElementById("adat4").value);

            let megtett = oraallas2 - oraallas1
            let fogyasztas = mennyi / megtett
            let fizettem = megtett * fogyasztas * ar

            document.getElementById("valasz").innerHTML=`a két utolsó tankolás között megtett út nagysága ${megtett} km`
            document.getElementById("valasz2").innerHTML=`100 km-re jutó fogyasztás nagysága ${fogyasztas*100} liter/100 km`
            document.getElementById("valasz3").innerHTML=`az 1 km-re jutó üzemanyagköltség összege ${fizettem} Ft/km).`
}