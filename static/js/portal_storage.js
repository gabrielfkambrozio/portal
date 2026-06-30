const PortalStorage = {
  prefix: "portal_livia_",

  key(modulo) {
    return `${this.prefix}${modulo}`;
  },

  listar(modulo) {
    const bruto = localStorage.getItem(this.key(modulo));
    if (!bruto) return [];

    try {
      return JSON.parse(bruto);
    } catch {
      return [];
    }
  },

  salvar(modulo, dados) {
    localStorage.setItem(this.key(modulo), JSON.stringify(dados));
  },

  adicionar(modulo, item) {
    const dados = this.listar(modulo);

    const novoItem = {
      id: crypto.randomUUID(),
      criado_em: new Date().toISOString(),
      ...item
    };

    dados.unshift(novoItem);
    this.salvar(modulo, dados);

    return novoItem;
  },

  atualizar(modulo, id, novosDados) {
    const dados = this.listar(modulo).map((item) => {
      if (item.id !== id) return item;

      return {
        ...item,
        ...novosDados,
        atualizado_em: new Date().toISOString()
      };
    });

    this.salvar(modulo, dados);
  },

  remover(modulo, id) {
    const dados = this.listar(modulo).filter((item) => item.id !== id);
    this.salvar(modulo, dados);
  },

  limpar(modulo) {
    localStorage.removeItem(this.key(modulo));
  }
};