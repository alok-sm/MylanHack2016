$(function(){
    $("#country-input").select2();
    $('#disease-input').select2({
        placeholder: "Select a Disease"
    });
    $('#state-input').select2({
        placeholder: "Select a State"
    });
    var sltext = '<option value="Bm">Bombali District</option><option value="Ko">Koinadugu District</option><option value="Po">Port Loko District</option><option value="To">Tonkolili District</option><option value="Ka">Kambia District</option><option value="Ke">Kenema District</option><option value="Kn">Kono District</option><option value="Kl">Kailahun District</option><option value="Bo">Bo District</option><option value="Bn">Bonthe District</option><option value="Pu">Pujehun District</option><option value="Mo">Moyamba District</option><option value="Wu">Western Area Urban District</option><option value="Wr">Western Area Rural District</option>'
    var intext = '<option value="Up">Uttar Pradesh</option><option value="Mh">Maharashtra</option><option value="Bi">Bihar</option><option value="Wb">West Bengal</option><option value="Mp">Madhya Pradesh</option><option value="Tn">Tamil Nadu</option><option value="Rj">Rajasthan</option><option value="Ka">Karnataka</option><option value="Gj">Gujarat</option><option value="Ap">Andhra Pradesh</option><option value="Od">Odisha</option><option value="Ts">Telangana</option><option value="Kl">Kerala</option><option value="Jk">Jharkhand</option><option value="As">Assam</option><option value="Pn">Punjab</option><option value="Ch">Chhattisgarh</option><option value="Hr">Haryana</option><option value="Jk">Jammu and Kashmir</option><option value="Uk">Uttarakhand</option><option value="Hp">Himachal Pradesh</option><option value="Tr">Tripura</option><option value="Mg">Meghalaya</option><option value="Mn">Manipur</option><option value="Ng">Nagaland</option><option value="Ga">Goa</option><option value="Ar">Arunachal Pradesh</option><option value="Mz">Mizoram</option><option value="Sk">Sikkim</option><option value="Dl">National Capital Region</option>'
    var pktext = '<option value="Ba">Balochistan</option><option value="Kh">Khyber Pakhtunkhwa</option><option value="Pu">Punjab</option><option value="Si">Sindh</option><option value="Ca">Capital Territory</option><option value="Tr">Tribal areas</option><option value="Az">Azad Kashmir</option><option value="Gi">Gilgit–Baltistan</option>'

    var countryCode;
    var stateCode;

    $('#country-input').change(function(event){
        // countryCode = event.target.value; 
        // console.log("country=" + "http://localhost:5000/" + event.target.value);
        // $.getJSON( "http://localhost:5000/" + event.target.value, function(data) {
        //     // console.log(data);
        //     alert(data)
        // });
        var xhr = new XMLHttpRequest();
        // var e = document.getElementById("country-code");
        // var countryChosen = e.options[e.selectedIndex].value;
        xhr.open("GET","http://localhost:5000/"+ event.target.value, false);
        xhr.send();
        console.log(xhr.responseText);
        // $.get("http://localhost:5000/" + event.target.value, function(data, status){
        //     alert("Data: " + data + "\nStatus: " + status);
        // });
        setupData(JSON.parse(xhr.responseText));
        switch(event.target.value){
            case 'PK': $('#state-input').html(pktext); break;
            case 'IN': $('#state-input').html(intext); break;
            case 'SL': $('#state-input').html(sltext); break;
            default  : $('#state-input').html('');     break;
        }
        return;
    });
});

