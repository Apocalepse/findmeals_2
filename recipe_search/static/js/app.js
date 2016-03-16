
angular.module('RecipeSearchApp').controller('RecipeSearch', function($scope, $http, $window, djangoForm) {
    $scope.submit = function() {
        if ($scope.search_data) {

            $scope.recipes = [];

            $http.post(".", $scope.search_data).success(function(out_data) {
                if (!djangoForm.setErrors($scope.search_form, out_data.errors)) {
                    angular.forEach(out_data, function(value, key) {
                        $scope.recipes.push(value)
                    });
                    console.log($scope.recipes);
                }
            }).error(function() {
                console.error('Error');
            });
        }
        return false;
    };
});
