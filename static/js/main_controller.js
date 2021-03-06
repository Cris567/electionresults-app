var app = angular.module('elections-app', ['chart.js']);

app.controller("main-controller", function ($scope, $http) {
  var provinces = [];
  var totalVotes = [];
  $scope.series = ['Erststimmen', 'Zweitstimmen'];
  $scope.toggle = false;

    $http.get('/getProvinces').success(function(response) {
      provinces = response;
      $scope.provinces = provinces;
    }).error(function(response) {
      console.log(response);
    });

    $scope.displayCounties = function (id) {
      var counties = [];

        $http.get('/getCounties?provinceId=' + id).success(function (response) {
          $scope.counties = response;
          for (var p in provinces) {
            if (provinces[p].p_id === id) {
              $scope.selectedProvince = provinces[p].p_name;
            }
          }
          }).error(function (response) {
              console.log(response);
          });
    };

    $scope.displayVotes = function (id, partyId) {
    let parties = [];
    let labels = [];
    $scope.votesInNumbers = [];
    let votesInNumbers1 = [];
    let votesInNumbers2 = [];

        $http.get('/getResultsByCountyPartyId?countyId=' + id).success(function (response) {
          let votes = response;
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
          for (c in $scope.counties) {
            if ($scope.counties[c].c_id === id) {
              $scope.selectedCounty = $scope.counties[c].c_name;
            }
          }
          $scope.parties = parties;
          $scope.labels = labels;
          $scope.votesInNumbers.push(votesInNumbers1);
          $scope.votesInNumbers.push(votesInNumbers2);
          $scope.toggle = true;
          }).error(function (response) {
              console.log(response);
          });
    };
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
