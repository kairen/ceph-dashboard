$(function () {
        //DONUT CHART
        var donut = new Morris.Donut({
          element: 'host_state',
          resize: true,
          colors: ["#cd2626", "#00a65a"],
          data: [
            {label: "MON", value: 2},
            {label: "OSD", value: 3}
          ],
          hideHover: 'auto'
        });
});