import "../../persistence/in-memory/seed";
import express from "express";
import contasController from "./controllers/contas";
import transacoesController from "./controllers/transacoes";
import funcionariosController from "./controllers/funcionarios";
import authController from "./controllers/auth";
import { getAuthUser } from "./middlewares/auth";
import { Pessoa } from "@/domain/pessoa/pessoa.entity";
import { Funcionario } from "@/domain/funcionario/funcionario.entity";

declare global {
  namespace Express {
    export interface Request {
      pessoa?: Pessoa | Funcionario;
    }
  }
}

const app = express();

app.use(express.json());

app.use("/auth", authController);
app.use("/contas", getAuthUser, contasController);
app.use("/transacoes", getAuthUser, transacoesController);
app.use("/funcionarios", getAuthUser, funcionariosController);

app.use((err: any, req: any, res: any, next: any) => {
  console.log(err);
  res.status(500).json({ name: err.name, message: err.message });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
