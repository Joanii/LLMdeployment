from langchain.llms import OpenLLM
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


if __name__ == '__main__':
    server_url = "http://localhost:3000"  # Replace with remote host if you are running on a remote server
    llm = OpenLLM(
        model_name="dolly-v2",
        model_id="databricks/dolly-v2-3b",
        temperature=0.94,
        repetition_penalty=1.2,
    )


    template = "What is a good name for a startup that creates {product}?"

    prompt = PromptTemplate(template=template, input_variables=["product"])

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    generated = llm_chain.run(product="AI models")
    print(generated)

