async function carregarConvivencias() {

    const { data, error } = await supabaseClient
        .from("convivencias")
        .select("*")
        .order("data", { ascending: true });


    if (error) {
        console.log(error);
        return;
    }


    const lista = document.querySelector("#lista-convivencias");


    data.forEach(convivencia => {

        lista.innerHTML += `
            <li>
                <strong>${convivencia.data}</strong>
                <br>
                ${convivencia.descricao}
                <br>
                Local: ${convivencia.local}
            </li>
        `;

    });

}


carregarConvivencias();