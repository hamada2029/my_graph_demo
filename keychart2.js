/*globals Chart Papa*/

var config = {};
config.type = 'line';
config.data = {};
config.data.labels = ['6月度', '7月度', '8月度', '9月度','10月度','11月度','12月度', '1月度', '2月度', '3月度', '4月度', '5月度(決算)'];
config.data.datasets = [{}];

config.data.datasets[0].label = '';  // '今期';
config.data.datasets[0].data = [];
config.data.datasets[0].borderColor = 'rgba(0,191,255,1)';
config.data.datasets[0].backgroundColor = 'rgba(0,0,255,0)';
config.data.datasets[0].lineTension = 0;
// データラベル設定
config.data.datasets[0].datalabels = {
    color: 'rgba(250,128,114,1)',
    font: {weight: 'bold', size: 20},
    anchor: 'end', // データラベルの位置（'end' は上端）
    align: 'end', // データラベルの位置（'end' は上側）
    padding: {bottom: 20},
    formatter: function (value) {
        // データラベルに文字などを付け足す
        return value + '%';
    }
};
// XX.X%
//var yVals = [0.218546468,0.260119402,0.273937151,0.233946978].map(x => (Math.round(x * 1000) / 10).toFixed(1));
var yVals = [];

config.options = {
    title: {
        display: false,
        text: '2. 売上高人件費比率'
    },
    scales: {
        yAxes: [{
            ticks: {
                suggestedMax: 30,
                suggestedMin: 0,
                stepSize: 10,
                callback: function(value) {
                    return value + '%';
                }
            }
        }]
    },
    // animation: false
};

var ctx = document.getElementById('myLineChart');
ctx.style.backgroundColor = 'rgba(240,240,240,255)';
var myLineChart = new Chart(
    ctx,
    config
);

var per1 = document.getElementById('per1');
var per2 = document.getElementById('per2');
var per3 = document.getElementById('per3');


var inp1 = document.getElementById('inp1');

function doit(yVals){
    config.data.datasets[0].data = [];
    myLineChart.update();
    var i = 0;
    var sid = setInterval(
        function(){
            config.data.datasets[0].data.push(yVals[i]);
            myLineChart.update();
            if(per1){
                per1.innerText = yVals[i];
                per2.innerText = yVals[i];
                per3.innerText = '0.0';
            }
            i++;
            if(i >= yVals.length){
                clearInterval(sid);
                console.log('cleared: ' + sid);
                inp1.value = '';
            }
        },
        1000
    );
}




function loadLocalFile(e) {
    // ファイル情報を取得
    var fileData = e.target.files[0];
    console.log(fileData); // 取得した内容の確認用

    // CSVファイル以外は処理を止める
    // if(!fileData.type.match('/csv')) {
    //     alert('csvファイルを選択してください');
    //     return;
    // }

    Papa.parse(
        e.target.files[0],
        {
            encoding: 'Shift-JIS',
            complete: function(results) {
                console.log(results);
                config.data.datasets[0].data = [];
                myLineChart.update();
                var r1 = results.data[0];
                var r2 = results.data[1];
                config.options.title.text = r1[0];
                config.data.labels = r1.slice(1, r1.length);
                config.data.datasets[0].label = r2[0];
                yVals = [];
                for(var i = 1; i < r2.length; i++){
                    if(r2[i].length == 0){continue;}  // 空文字
                    yVals.push(
                        (Math.round(r2[i] * 1000) / 10).toFixed(1)
                    );
                }
                myLineChart.update();
                doit(yVals);
            }
        }
    );
}

inp1.addEventListener('change', loadLocalFile, false);


