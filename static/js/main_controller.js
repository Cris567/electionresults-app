var app = angular.module('elections-app', ['chart.js']);

app.controller("main-controller", function ($scope, $http) {
  // var provinces = [];
  var votes = [];
  var parties = [];
  var labels = [];
  var totalVotes = [];
  var votesInNumbers1 = [];
  var votesInNumbers2= [];
  var percentages = [];

    $http.get('/getProvinces').success(function(response) {
      // for (var i = 0; i < response.length; i++) {
      //   provinces[i] = response[i].p_name;
      // }
      $scope.provinces = response;
    }).error(function(response) {
      console.log(response);
    });

    $scope.displayCounties = function (id) {
      var counties = [];

        $http.get('/getCounties?provinceId=' + id).success(function (response) {
          counties = response;
          $scope.counties = counties;
          }).error(function (response) {
              console.log(response);
          });
    };

    $scope.displayVotes = function (id, partyId) {
    parties = [];
    labels = [];
    votesInNumbers1 = [];
    votesInNumbers2 = [];

        $http.get('/getResultsByCountyPartyId?countyId=' + id).success(function (response) {
          votes = response;
          $scope.votes = votes;
          totalVotes[0] = votes[3].e_current;
          totalVotes[1] = votes[3].z_current;
          for (var v = 4; v < votes.length; v++) {
            if (votes[v].e_current != "" && votes[v].z_current != "" && votes[v].province_id != 99) {
              let perc_e = parseFloat((votes[v].e_current / totalVotes[0]) * 100).toFixed(2);
              let perc_z = parseFloat((votes[v].z_current / totalVotes[1]) * 100).toFixed(2);
              votes[v].perc_e = perc_e;
              votes[v].perc_z = perc_z;
              votesInNumbers1.push(votes[v].e_current);
              votesInNumbers2.push(votes[v].z_current);
              labels.push(votes[v].party_name);
              parties.push(votes[v]);
            }
          }
          $scope.parties = parties;
          $scope.labels = labels;
          $scope.votesInNumbers1 = votesInNumbers1;
          $scope.votesInNumbers2 = votesInNumbers2;
          console.log(labels);
          }).error(function (response) {
              console.log(response);
          });
    };

    // function getPartyNames(parties) {
    //   var arrayBla = [];
    //
    //   $http.get('/getParties').success(function (response) {
    //     console.log(response);
    //   for (var p in parties) {
    //     var p_id = parties[p].party_id;
    //     arrayBla.push(p_id);
    //   }
    //   }).error(function (response) {
    //       console.log(response);
    //   });
    //   console.log(arrayBla);
    //   return arrayBla;
    // }
    //
    // $scope.labels = getPartyNames(parties);

    // $scope.votesInNumbers = partyVotes.perc_e;

});

function search() {
  var searchBar = document.getElementById("search-input").value.toUpperCase();
  var listitems = document.getElementById("countylist").getElementsByTagName("li");
  for (var i in listitems) {
      var link = listitems[i].getElementsByTagName("a")[0];
      var query = link.textContent || link.innerText;
      if (query.toUpperCase().indexOf(searchBar) > -1) {
          listitems[i].style.display = "";
      } else listitems[i].style.display = "none";
  }
}
