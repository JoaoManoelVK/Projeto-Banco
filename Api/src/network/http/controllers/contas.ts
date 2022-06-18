import { CriarContaCorrenteStory } from "@/domain/conta-corrente/stories/criar-conta.story";
import { CriarContaPoupancaStory } from "@/domain/conta-poupanca/stories/criar-conta-poupanca.story";
import { GetContasStory } from "@/domain/conta/stories/get-contas.story";
import { AgenciaInMemoryRepository } from "@/persistence/in-memory/agencia.repository";
import { ContaCorrenteInMemoryRepository } from "@/persistence/in-memory/conta-corrente.repository";
import { ContaPoupancaInMemoryRepository } from "@/persistence/in-memory/conta-poupanca.repository";
import { ContaInMemoryRepository } from "@/persistence/in-memory/conta.repository";
import { PessoaInMemoryRepository } from "@/persistence/in-memory/pessoa.repository";
import { Router } from "express";
import { validarPermissoes } from "../middlewares/auth";

const router = Router();

router.get("/", async (req, res, next) => {
  try {
    const contasRepository = ContaInMemoryRepository.get();
    const story = new GetContasStory(contasRepository);

    res.status(200).json(await story.execute());
  } catch (error) {
    next(error);
  }
});

router.post(
  "/corrente",
  validarPermissoes((p) => p.has("conta.criar")),
  async (req, res, next) => {
    try {
      const story = new CriarContaCorrenteStory(
        ContaCorrenteInMemoryRepository.get(ContaInMemoryRepository.get()),
        AgenciaInMemoryRepository.get(),
        PessoaInMemoryRepository.get()
      );

      const result = await story.execute(req.body);

      res.status(201).json(result);
    } catch (error) {
      next(error);
    }
  }
);

router.post(
  "/poupanca",
  validarPermissoes((p) => p.has("conta.criar")),
  async (req, res, next) => {
    try {
      const story = new CriarContaPoupancaStory(
        ContaPoupancaInMemoryRepository.get(ContaInMemoryRepository.get()),
        AgenciaInMemoryRepository.get(),
        PessoaInMemoryRepository.get()
      );

      const result = await story.execute(req.body);

      res.status(201).json(result);
    } catch (error) {
      next(error);
    }
  }
);

export default router;
