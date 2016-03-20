$(function(){

    function getColor(intensity){
        return '#' + get2DigitHex(intensity) + get2DigitHex(100 - intensity) + '00'
        // return 'red';
    }

    function get2DigitHex(intensity){
        ret = Number(Math.floor(intensity/100 * 255)).toString(16)
        if(ret.length == 1){
            ret = '0' + ret;
        }
        return ret;
    }

    function setThreatLevel(val){
    var percent_number_step = $.animateNumber.numberStepFactories.append(' %')
    $('#fun-level').animateNumber(
        {
            number: val,
            color: getColor(val),
            easing: 'easeInQuad',
            numberStep: percent_number_step
        },
        4000
    );
}
    // $("#fun-level").animate({ color: "blue" }, 10000);

    // $('#country-input').select2({
    //     placeholder: 'Select Country'
    // });
    $('#state-input').select2({
        placeholder: 'Select State'
    });
    var sltext = '<option value="all">All Districts</option><option value="Bm">Pujehun District</option><option value="Ko">Bonthe District</option><option value="Po">Kenema District</option><option value="To">Bo District</option><option value="Ka">Moyamba District</option><option value="Ke">Kailahun District</option><option value="Kn">Western Area Rural District</option><option value="Kl">Kono District</option><option value="Bo">Western Area Urban District</option><option value="Bn">Tonkolili District</option><option value="Pu">Port Loko District</option><option value="Mo">Bombali District</option><option value="Wu">Kambia District</option><option value="Wr">Koinadugu District</option>'
    var intext = '<option value="Up">Uttar Pradesh</option><option value="Mh">Maharashtra</option><option value="Bi">Bihar</option><option value="Wb">West Bengal</option><option value="Mp">Madhya Pradesh</option><option value="Tn">Tamil Nadu</option><option value="Rj">Rajasthan</option><option value="Ka">Karnataka</option><option value="Gj">Gujarat</option><option value="Ap">Andhra Pradesh</option><option value="Od">Odisha</option><option value="Ts">Telangana</option><option value="Kl">Kerala</option><option value="Jk">Jharkhand</option><option value="As">Assam</option><option value="Pn">Punjab</option><option value="Ch">Chhattisgarh</option><option value="Hr">Haryana</option><option value="Jk">Jammu and Kashmir</option><option value="Uk">Uttarakhand</option><option value="Hp">Himachal Pradesh</option><option value="Tr">Tripura</option><option value="Mg">Meghalaya</option><option value="Mn">Manipur</option><option value="Ng">Nagaland</option><option value="Ga">Goa</option><option value="Ar">Arunachal Pradesh</option><option value="Mz">Mizoram</option><option value="Sk">Sikkim</option><option value="Dl">National Capital Region</option>'
    var pktext = '<option value="Ba">Balochistan</option><option value="Kh">Khyber Pakhtunkhwa</option><option value="Pu">Punjab</option><option value="Si">Sindh</option><option value="Ca">Capital Territory</option><option value="Tr">Tribal areas</option><option value="Az">Azad Kashmir</option><option value="Gi">Gilgit–Baltistan</option>'

    var countryCode;
    var stateCode;
    var alldata;
    document.getElementById("month").value = 1;
    $("#month").change(function(event){
        setupData(alldata[event.target.value-1]);
switch(event.target.value){
    case 1: setThreatLevel(66); break;
    case 2: setThreatLevel(56); break;
    case 3: setThreatLevel(41); break;
    case 4: setThreatLevel(16); break;
}
        
    });
    $('#country-input').change(function(event){
        // countryCode = event.target.value; 
        // console.log("country=" + "http://localhost:5000/" + event.target.value);
        // $.getJSON( "http://localhost:5000/" + event.target.value, function(data) {
        //     // console.log(data);
        //     alert(data)
        // });
        switch(event.target.value){
            case 'PK': $('#state-input').html(pktext); break;
            case 'IN': $('#state-input').html(intext); break;
            case 'SL': $('#state-input').html(sltext); 
                var xhr = new XMLHttpRequest();
                // var e = document.getElementById("country-code");
                // var countryChosen = e.options[e.selectedIndex].value;
                xhr.open("GET","http://localhost:5000/"+ event.target.value, false);
                xhr.send();
                setThreatLevel(0);
                console.log(xhr.responseText);
                // $.get("http://localhost:5000/" + event.target.value, function(data, status){
                //     alert("Data: " + data + "\nStatus: " + status);
                // });
                alldata = JSON.parse(xhr.responseText);
                // alldata = alldata.reverse();
                ind = document.getElementById("month").value;
                setupData(alldata[ind-1]);
            break;
            default  : $('#state-input').html('');     break;
        }
        return;
    });
    $('#state-input').change(function(event){
        if(event.target.selectedIndex == 0){
            setThreatLevel(0);    
            resetPolygons();
        }
        else{
        setThreatLevel(data[event.target.selectedIndex-1]*100);
        fadeOneIn(event.target.selectedIndex-1);
    }
    });
});

