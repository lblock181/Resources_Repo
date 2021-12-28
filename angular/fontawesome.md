## Adding Fontawesome to Angular project

- Documentation Github link
 > https://github.com/FortAwesome/angular-fontawesome

 1. Run command below
	`npm install @fortawesome/fontawesome-svg-core
	npm install @fortawesome/free-solid-svg-icons
	npm install @fortawesome/angular-fontawesome@0.9.0`
 2. Add FontAwesomeModule to imports in src/app/app.module.ts
	`import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';`
	`FontAwesomeModule`

### Usage
 1. Tie the icon to the property in your component. Ensure icon is named in component
 2. Add component name & tie to imported name within the export Class portion
	`faCoffee = faCoffee;`

[In-depth Usage](https://github.com/FortAwesome/angular-fontawesome/blob/master/docs/usage.md)
