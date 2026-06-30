const PortalStorage = {

    prefix: "portal_lg_",

    chave(modulo) {
        return this.prefix + modulo;
    },

    listar(modulo) {

        const dados = localStorage.getItem(this.chave(modulo));

        if (!dados) {
            return [];
        }

        try {
            return JSON.parse(dados);
        } catch (e) {
            return [];
        }

    },

    salvar(modulo, lista) {

        localStorage.setItem(
            this.chave(modulo),
            JSON.stringify(lista)
        );

    },

    adicionar(modulo, item) {

        const lista = this.listar(modulo);

        item.id = Date.now();

        lista.push(item);

        this.salvar(modulo, lista);

        return item;

    },

    buscar(modulo, id) {

        const lista = this.listar(modulo);

        return lista.find(v => Number(v.id) === Number(id));

    },

    atualizar(modulo, id, dados) {

        const lista = this.listar(modulo);

        const indice = lista.findIndex(
            v => Number(v.id) === Number(id)
        );

        if (indice === -1) {
            return false;
        }

        lista[indice] = {
            ...lista[indice],
            ...dados
        };

        this.salvar(modulo, lista);

        return true;

    },

    remover(modulo, id) {

        const lista = this
            .listar(modulo)
            .filter(v => Number(v.id) !== Number(id));

        this.salvar(modulo, lista);

    },

    limpar(modulo) {

        localStorage.removeItem(
            this.chave(modulo)
        );

    }

};