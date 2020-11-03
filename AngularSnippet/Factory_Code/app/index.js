var app = angular.module("myApp", []);

app.service("MathFactory", function () {
  this.add = function (a, b) {
    return a + b;
  };

  this.subtract = function (a, b) {
    return a - b;
  };

  this.multiply = function (a, b) {
    return a * b;
  };

  this.divide = function (a, b) {
    return a / b;
  };
});

app.service("CalculatorFactory", function (MathFactory) {
  this.square = function (a) {
    return MathFactory.multiply(a, a);
  };
  this.cube = function (a) {
    return MathFactory.multiply(a, MathFactory.multiply(a, a));
  };
});

app.controller("CalculatorController", function ($scope, CalculatorFactory) {
  $scope.Square = function () {
    $scope.answer = CalculatorFactory.square($scope.num);
  };

  $scope.Cube = function () {
    $scope.answer = CalculatorFactory.cube($scope.num);
  };
});
