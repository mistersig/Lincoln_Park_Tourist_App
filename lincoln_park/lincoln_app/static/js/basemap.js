{% extends "base.html" %}

function createMap(){

var mymap = L.map('mapid').setView([41.918873, -87.631077], 15); //38.724066, -99.262098 //

var Hydda_Full = L.tileLayer('https://{s}.tile.openstreetmap.se/hydda/full/{z}/{x}/{y}.png', {
  maxZoom: 18,
  attribution: 'Tiles courtesy of <a href="http://openstreetmap.se/" target="_blank">OpenStreetMap Sweden</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(mymap)

  var geojsonMarkerOptions = {
    radius: 15,
    fillColor: "#fffa0a",
    color: "#000cff",
    weight: 1,
    opacity: 1,
    fillOpacity: .8
  };
getData(mymap)
// createVideoPopUps("{{data|safe}}",mymap)
// map_init_basic(mymap,geojsonMarkerOptions)
}; //end of create map


function getData(mymap){
  // console.log("{{data | safe}}");
  // the_data = widget.init(data_from_django);
  // data_from_django = "{{data | safe}}";
  // the_data = widget.init(data_from_django);
  
  // need to remove the quotes and shit from query
  var the_data = {{ data|safe }};
  console.log(the_data);
  // load the data

  $.ajax({
    // url:'http://127.0.0.1:8000/artist/',
    type: 'GET',
    // dataType:"json",
    data:the_data,
    success: function(response){
      console.log('trying');
      createVideoPopUps(the_data,mymap);
    } //end of success 
  });
};//end of getData




function createVideoPopUps(response,mymap){
  console.log('working on popups')
  
  console.log(response);
  var geojsonMarkerOptions = {
    radius: 15,
    fillColor: "#fffa0a",
    color: "#000cff",
    weight: 1,
    opacity: 1,
    fillOpacity: .8
  };

// art_name: "The Alarm"
// artist_name: "John J. Boyle"
// latitude: 41.936633
// longitude: -87.635884
// park_name: "LINCOLN (ABRAHAM)"
// park_number: 100

  var layer = L.geoJSON(response, {pointToLayer: function (feature, latlng) {

    var popUpContent = feature.properties["art_name"];
    // console.log(feature);
    // popUpContent += feature.properties["artist_name"];
    layer = L.circleMarker(latlng,geojsonMarkerOptions);
    layer.bindPopup(popUpContent,{offset: new L.point(0,0), maxWidth: 560
    });
        layer.on({
    mouseover: function(){
        this.openPopup();
    },
    // mouseout: function(){
    //     this.closePopup();
    // },
    click: function(){
        layer.on(popUpContent);
    }
    });
    // return L.circleMarker(latlng, geojsonMarkerOptions).addTo(mymap);
    return layer.addTo(mymap);
  }
  })
};//end createVideoPopUps


$(document).ready(createMap);

















// function createMap(){

// var mymap = L.map('mapid').setView([41.918873, -87.631077], 15); //38.724066, -99.262098 //
// // var Stamen_TonerLite = L.tileLayer(
// // 	'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}{r}.{ext}', 
// // 	{ attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
// // 	subdomains: 'abcd',
// // 	minZoom: 0,
// // 	maxZoom: 20,
// // 	ext: 'png'

// var Hydda_Full = L.tileLayer('https://{s}.tile.openstreetmap.se/hydda/full/{z}/{x}/{y}.png', {
// 	maxZoom: 18,
// 	attribution: 'Tiles courtesy of <a href="http://openstreetmap.se/" target="_blank">OpenStreetMap Sweden</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
// }).addTo(mymap)

// 	var geojsonMarkerOptions = {
//     radius: 15,
//     fillColor: "#fffa0a",
//     color: "#000cff",
//     weight: 1,
//     opacity: 1,
//     fillOpacity: .8
// 	};
// getData(mymap)
// // map_init_basic(mymap,geojsonMarkerOptions)
// }; //end of create map

// // "{% url 'points' %}"


// // function map_init_basic (map, options) {

// //    var geojsonPointLayer = new L.GeoJSON.AJAX("{% url 'markers' %}", {
// //        onEachFeature:function(feature, layer) {
// //             layer.bindPopup(feature.properties.name.toString());
// //         }
// //     });
// //    geojsonPointLayer.addTo(map);
// // };//end of map_init_basic

// // "{% static "leaflet/leaflet.css"%}"
// function getData(mymap){
// 	var dataJson = "{{markers}}";
// 	console.log(dataJson);

// 	$.ajax(dataJson,{
// 		dataType:"json",
// 		success: function(response){
// 			console.log(response)
// 			createVideoPopUps(response,mymap);
// 		} //end of success 
// 	});
// };//end of getData


// function showLandMarks(selType) {
//   $.ajax({
//     url: 'HttpServlet',
//     type: 'POST',
//     data: { "tab_id": "1", "type": selType},
//     success: function(landmarks) { 
//       mapInitialization(landmarks);
//     },
//     error: function(xhr, status, error) {
//       alert("An AJAX error occured: " + status + "\nError: " + error);
//     }
//   });
// } // end of showAllLandMarks



// function createVideoPopUps(response,mymap){
// 	// console.log(response);
// 	// var popUpContent = "<p><b>City: <b>" +response.features.properties["City"]+ "</p>";
// 	//console.log(popUpContent);
// 	// console.log("trying in create createVideoPopUps");
// 	console.log(response);
// 	var geojsonMarkerOptions = {
//     radius: 15,
//     fillColor: "#fffa0a",
//     color: "#000cff",
//     weight: 1,
//     opacity: 1,
//     fillOpacity: .8
// 	};

// 	var layer = L.geoJSON(response, {pointToLayer: function (feature, latlng) {
// 		var popUpContent = feature.properties["geoid"];
// 		console.log(feature);
// 		popUpContent += feature.properties["artist_name"];
// 		layer = L.circleMarker(latlng,geojsonMarkerOptions);
// 		layer.bindPopup(popUpContent,{offset: new L.point(0,0), maxWidth: 560
// 		});
// 		    layer.on({
//     mouseover: function(){
//         this.openPopup();
//     },
//     // mouseout: function(){
//     //     this.closePopup();
//     // },
//     click: function(){
//         layer.on(popUpContent);
//     }
//     });
// 		// return L.circleMarker(latlng, geojsonMarkerOptions).addTo(mymap);
// 		return layer.addTo(mymap);
// 	}
// 	})
// };//end createVideoPopUps


// $(document).ready(createMap);


// //ZB Installations throughout US
// //Alan Ross Machinery 
// function createMap(){
// var mymap = L.map('mapid').setView([38.505, -99.09], 4); //38.724066, -99.262098 //
// var Stamen_TonerLite = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}{r}.{ext}', {
// 	attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
// 	subdomains: 'abcd',
// 	minZoom: 0,
// 	maxZoom: 5,
// 	ext: 'png'
// }).addTo(mymap);

// // var Stamen_Watercolor = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {
// // 	attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
// // 	subdomains: 'abcd',
// // 	minZoom: 0,
// // 	maxZoom: 7,
// // 	ext: 'png'
// // }).addTo(mymap);
// getData(mymap)
// };//end of create map function 
// function getData(mymap){
// 	// load the data
// 	$.ajax("data/zbInstalls.geojson",{
// 		dataType:"json",
// 		success: function(response){
// 			//console.log(response)
// 			createVideoPopUps(response,mymap);
// 		} //end of success 
// 	});
// };//end of getData
// function createVideoPopUps(response,mymap){
// 	// console.log(response);
// 	// var popUpContent = "<p><b>City: <b>" +response.features.properties["City"]+ "</p>";
// 	//console.log(popUpContent);
// 	var geojsonMarkerOptions = {
//     radius: 15,
//     fillColor: "#fffa0a",
//     color: "#000cff",
//     weight: 1,
//     opacity: 1,
//     fillOpacity: .8
// 	};
// 	var layer = L.geoJSON(response, {pointToLayer: function (feature, latlng) {
// 		var popUpContent = feature.properties["Notes"];
// 		console.log(feature);
// 		popUpContent += feature.properties["Url"];
// 		layer = L.circleMarker(latlng,geojsonMarkerOptions);
// 		layer.bindPopup(popUpContent,{offset: new L.point(0,0), maxWidth: 560
// 		});
// 		    layer.on({
//     mouseover: function(){
//         this.openPopup();
//     },
//     // mouseout: function(){
//     //     this.closePopup();
//     // },
//     click: function(){
//         layer.on(popUpContent);
//     }
//     });
// 		// return L.circleMarker(latlng, geojsonMarkerOptions).addTo(mymap);
// 		return layer.addTo(mymap);
// 	}
// 	})
// };//end createVideoPopUps
// $(document).ready(createMap);