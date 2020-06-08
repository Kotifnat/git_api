$(function() {
//   (function(name) {
//     var container = $('#pagination-' + name);
//     var sources = function () {
//       var result = [];

//       for (var i = 1; i < 196; i++) {
//         result.push(i);
//       }

//       return result;
//     }();
// 		console.log(sources)

//     var options = {
//       dataSource: sources,
//       callback: function (response, pagination) {
//         window.console && console.log(response, pagination);

//         var dataHtml = '<ul>';

//         $.each(response, function (index, item) {
//           dataHtml += '<li>' + item + '</li>';
//         });

//         dataHtml += '</ul>';

//         container.prev().html(dataHtml);
//       }
//     };

//     //$.pagination(container, options);

//     container.addHook('beforeInit', function () {
//       window.console && console.log('beforeInit...');
//     });
//     container.pagination(options);

//     container.addHook('beforePageOnClick', function () {
//       window.console && console.log('beforePageOnClick...');
//       //return false
//     });
//   })('demo1');

  (function(name) {
    var container = $('#pagination-' + name);
    container.pagination({
      dataSource: ,
      locator: 'items',
      totalNumber: 50,
      pageSize: 10,
			showPageNumbers: true,
			showPrevious: true,
			showNext: true,
			showNavigator: true,
			showFirstOnEllipsisShow: true,
			showLastOnEllipsisShow: true,
      ajax: {
        beforeSend: function() {
          container.prev().html('Loading data from GitHub ...');
        }
      },
      callback: function(response, pagination) {
        var dataHtml = '<ul>';
        $.each(response, function (index, item) {
          dataHtml += '<li>' + item + '</li>';
        });
        dataHtml += '</ul>';
        container.prev().html(dataHtml);
      }
    })
  })('demo2');
})
