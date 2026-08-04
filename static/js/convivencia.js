async function carregarConvivencias() {

    const lista = document.getElementById("lista-convivencias");


    const { data, error } = await supabaseClient
        .from("convivencias")
        .select("*")
        .order("data", { ascending: true });


    if (error) {

        console.error(error);

        lista.innerHTML = `
            <li>
                Erro ao carregar convivências.
            </li>
        `;

        return;
    }


    lista.innerHTML = "";


    data.forEach(item => {


        const dataEvento = new Date(item.data);


        const dia = dataEvento
            .getDate()
            .toString()
            .padStart(2, "0");


        const mes = dataEvento
            .toLocaleDateString("pt-BR", {
                month: "short"
            })
            .replace(".", "")
            .toUpperCase();



        lista.innerHTML += `

            <li class="convivencia">


                <div class="data">

                    <span class="dia">
                        ${dia}
                    </span>

                    <span class="mes">
                        ${mes}
                    </span>

                </div>



                <div class="convivencia-info">


                    <h2>
                        Convivência de ${mes}
                    </h2>


                    <p>
                        ${item.descricao ?? "Descrição não informada"}
                    </p>


                    <span class="local">
                        📍 ${item.local ?? "Local em breve"}
                    </span>


                </div>


            </li>

        `;


    });


}


carregarConvivencias();