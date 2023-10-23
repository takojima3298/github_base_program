document.getElementById("dataForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const product_code_list_str = document.getElementById("productCode").value;
    fetchData(product_code_list_str);
});

async function fetchData(product_code_list_str) {
    await axios.get(`http://localhost:8000/base_api/01/${product_code_list_str.split(/\n/)}` )
        .then(response => {
            // レスポンスのデータを取得
            const get_data = response.data;
            /// オブジェクトの並列探索
            var table = document.getElementById('table1');  //表のオブジェクトを取得
            const len = table.rows.length ;
            for ( var i = 1 ; i < len -1 ; i ++ ) {
                const row_num = table.rows.length ;
                table.deleteRow ( row_num - 1 ) ;
            }
 
            for ( var $keyA in get_data ) {
                var row = table.insertRow(-1);  //行末に行(tr要素)を追加
                var cell1 = row.insertCell(0);  //セル(td要素)の追加
                var cell2 = row.insertCell(1); 
                var cell3 = row.insertCell(2); 
                var cell4 = row.insertCell(3); 
                var cell5 = row.insertCell(4); 
                var cell6 = row.insertCell(5); 
                document.getElementById("idf_check").textContent = get_data[$keyA]["idf_check"];
                
                cell1.innerHTML = get_data[$keyA]["product_code"]
                cell2.innerHTML = get_data[$keyA]["product_name"]
                cell3.innerHTML = get_data[$keyA]["sales_date"]
                cell4.innerHTML = get_data[$keyA]["quantity"]
                cell5.innerHTML = get_data[$keyA]["unit_price"]
                cell6.innerHTML = get_data[$keyA]["amount"]
            }
            }        )
        .catch(error => {
            // エラーが発生した場合の処理
            alert(error)
            showError(error.message);
        });
}
function showDataResult() {
    alert("vv")
    document.getElementById("dataResult").classList.remove("hidden");
}

function showError(message) {
    alert(`エラーが発生しました：${message}`);
}
