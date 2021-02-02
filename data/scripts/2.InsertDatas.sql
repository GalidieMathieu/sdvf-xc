LOAD DATA INFILE "/var/lib/mysql-files/ingredient_in_recipe.csv"
INTO TABLE `ingredient_in_recipe`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/ingredient_Type.csv"
INTO TABLE `Ingredient_Type`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/ingredient.csv"
INTO TABLE `ingredient`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/recipes.csv"
INTO TABLE `Recipes`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/regime_alimentaire.csv"
INTO TABLE `regime_alimentaire`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/regime_recette.csv"
INTO TABLE `regime_recette`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/regime_users.csv"
INTO TABLE `regime_users`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/relation_ingredient_user.csv"
INTO TABLE `relation_ingredient_user`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/var/lib/mysql-files/users.csv"
INTO TABLE `users`
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;






