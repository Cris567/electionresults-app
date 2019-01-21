var app = angular.module('elections-app', ['chart.js']);

app.controller("main-controller", function ($scope, $http) {
  // var provinces = [];
  var votes = [];
  var parties = [];
  var totalVotes = [];
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

        $http.get('/getResultsByCountyPartyId?countyId=' + id).success(function (response) {
          votes = response;
          $scope.votes = votes;
          totalVotes[0] = votes[3].e_current;
          totalVotes[1] = votes[3].z_current;
          for (var v = 4; v < votes.length; v++) {
            if (votes[v].e_current != "" && votes[v].z_current != "") {
              let perc_e = parseFloat((votes[v].e_current / totalVotes[0]) * 100).toFixed(2);
              let perc_z = parseFloat((votes[v].z_current / totalVotes[1]) * 100).toFixed(2);
              votes[v].perc_e = perc_e;
              votes[v].perc_z = perc_z;
              parties.push(votes[v]);
            }
          }
          $scope.parties = parties;
          }).error(function (response) {
              console.log(response);
          });
    };
});
