## Bootstrap Documents
 - [Getting Started](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
 - Requirements for using Bootstrap
 1. Must have HTML5 doctype
	`<!doctype html>
	<html lang="en">
	  ...
	</html>`
 2. Must have responsive width
	> <meta name="viewport" content="width=device-width, initial-scale=1">

## Angular
 1. Run command `npm i bootstrap jquery @popperjs/core`
 2. Open angular-cli.json
 3. Add following to styles section `"../node_modules/bootstrap/css/bootstrap.css"`
 4. Add following to scripts section
	`"../node_modules/jquery/dist/jquery.js",
        "../node_modules/popper.js/dist/umd/popper.js",
        "../node_modules/bootstrap/dist/js/bootstrap.js"`

## HTML
 - CSS
 > <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
 - JS Bundle (Popper & Bootstrap)
 > <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
 - Separate (Popper & Bootstrap)
 > <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
 > <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>


## Django
