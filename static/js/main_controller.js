var app = angular.module('elections-app', []);

app.controller("main-controller", function ($scope, $http) {
  // var provinces = [];

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

        $http.get('/getCounties').success(function (response) {
          for (var i = 0; i < response.length; i++) {
            if (response[i].c_belongs_to == id) {
              counties[i] = response[i];
            }
          }
          $scope.counties = counties;
          }).error(function (response) {
              console.log(response);
          });
};
});
