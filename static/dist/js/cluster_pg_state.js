$(function () {
        //DONUT CHART
        var donut = new Morris.Donut({
          element: 'pg_state',
          resize: true,
          colors: ["#cd2626", "#eba709", "#00a65a"],
          data: [
            {label: "Dirty", value: 63},
            {label: "Working", value: 100},
            {label: "Clean", value: 80}
          ],
          hideHover: 'auto'
        });
});