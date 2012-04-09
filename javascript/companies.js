function MyCompany() {
    this.url = 'mycompany.com';
};
MyCompany.prototype = new HTTP();
MyCompany.prototype.get('projects', 'employees', 'customers');

function YourCompany() {
    this.url = 'yourcompany.com';
}
YourCompany.prototype = new HTTP();
YourCompany.prototype.get('projects', 'employees');
