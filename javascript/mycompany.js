
function MyCompany() {
    this.url = 'mycompany.com';
};

MyCompany.prototype.projects = function() {
    return this._get('/projects');
}

MyCompany.prototype.employees = function() {
    return this._get('/employees');
}

MyCompany.prototype.customers = function() {
    return this._get('/customers');
}

MyCompany.prototype._get = function(path) {
    return 'GET ' + this.url + path;
}
