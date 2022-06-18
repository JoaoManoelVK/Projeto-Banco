import { Router } from "express";
import { AutenticarPessoaStory } from "@/domain/pessoa/stories/autenticar.story";
import { PessoaInMemoryRepository } from "@/persistence/in-memory/pessoa.repository";
import { getAuthUser } from "../middlewares/auth";

const router = Router();

router.post("/", async (req, res) => {
  try {
    const { cpf, senha } = req.body;
    const story = new AutenticarPessoaStory(PessoaInMemoryRepository.get());

    const result = await story.execute({ cpf, senha });

    res.status(200).json(result);
  } catch (error) {
    res
      .status(401)
      .json({ name: "AuthError", message: `CPF e/ou senha inválidos!` });
  }
});

router.get("/eu", getAuthUser);

export default router;
