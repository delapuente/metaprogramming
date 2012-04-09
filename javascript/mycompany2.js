function MyCompany() {
    this.url = 'mycompany.com';
};

function makeGet(path) {
    return function(){
        return 'GET ' + this.url + '/' + path;
    };
}

['projects', 'employees', 'customers'].forEach(function(name){
    MyCompany.prototype[name] = makeGet(name);
});
