import { Transacao } from "./transacao.entity";

export interface TransacaoRespository {
  create(transacao: Transacao): Promise<Transacao>;
  getAll(): Promise<Transacao[]>;
  getByConta(conta: number): Promise<Transacao[]>;
}
