import { CriarDepositoStory } from "@/domain/transacao/stories/criar-deposito.story";
import { CriarSaqueStory } from "@/domain/transacao/stories/criar-saque.story";
import { CriarTransferenciaStory } from "@/domain/transacao/stories/criar-transferencia.story";
import { ObterExtrato } from "@/domain/transacao/stories/obter-extrato.story";
import { ContaInMemoryRepository } from "@/persistence/in-memory/conta.repository";
import { TransacaoInMemoryRepository } from "@/persistence/in-memory/transacao.repository";
import { Router } from "express";

const router = Router();

router.post("/deposito", async (req, res, next) => {
  try {
    const story = new CriarDepositoStory(
      TransacaoInMemoryRepository.get(ContaInMemoryRepository.get()),
      ContaInMemoryRepository.get()
    );

    const result = await story.execute(req.body);

    res.status(201).json(result);
  } catch (error) {
    next(error);
  }
});

router.post("/transferencia", async (req, res, next) => {
  try {
    const story = new CriarTransferenciaStory(
      TransacaoInMemoryRepository.get(ContaInMemoryRepository.get()),
      ContaInMemoryRepository.get()
    );

    const result = await story.execute({
      ...req.body,
      titular: req.pessoa,
    });

    res.status(201).json(result);
  } catch (error) {
    next(error);
  }
});

router.post("/saque", async (req, res, next) => {
  try {
    const story = new CriarSaqueStory(
      TransacaoInMemoryRepository.get(ContaInMemoryRepository.get()),
      ContaInMemoryRepository.get()
    );

    const result = await story.execute({
      ...req.body,
      titular: req.pessoa,
    });

    res.status(201).json(result);
  } catch (error) {
    next(error);
  }
});

router.get("/extrato/:conta", async (req, res, next) => {
  try {
    const story = new ObterExtrato(
      TransacaoInMemoryRepository.get(ContaInMemoryRepository.get())
    );

    const result = await story.execute(+req.params.conta);

    res.status(200).json(result);
  } catch (error) {
    next(error);
  }
});

export default router;
