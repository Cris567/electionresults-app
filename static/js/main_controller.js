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

        $http.get('/getCounties?provinceId=' + id).success(function (response) {
          counties = response;
          $scope.counties = counties;
          }).error(function (response) {
              console.log(response);
          });
};
});
