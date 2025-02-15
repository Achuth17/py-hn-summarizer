Post: https://news.ycombinator.com/item?id=43053844

**Summary**

*   Fly.io invested in GPU Machines to enable AI/ML inference for developers, but this bet is not paying off as expected.
*   Building GPU Machines was complex and challenging due to security concerns and difficulties integrating Nvidia drivers with their micro-VM hypervisor.
*   The core issue is that most software developers are not interested in managing raw GPUs; they primarily want to use LLMs through APIs.
*   For developers focused on application development, managed LLM APIs from companies like OpenAI and Anthropic are sufficient and more convenient.
*   The demand for raw GPU instances on Fly.io is limited, as the market for developers wanting to manage their own GPU infrastructure is smaller than anticipated.
*   Fly.io is not abandoning GPUs entirely but is scaling back further development and investment in this area.
*   Key learnings include the shift in developer needs towards LLM APIs and the niche nature of the raw GPU market for their target audience.
*   Despite the outcome, Fly.io considers the GPU venture a valuable learning experience and highlights the importance of taking calculated risks and adapting based on market feedback.

**Discussion Summary**

*   **Positive Feedback on Fly GPU Machines** (<https://news.ycombinator.com/item?id=43054917>)
    *   Fly GPU machines are praised for being fantastic, extremely fast to start on-demand, and reliable.
    *   The developer experience (DX) is excellent, consistent with other Fly machines, making it easy to use with familiar commands.
    *   While considered a bit pricey, the cost is seen as reasonable compared to alternatives, with better reliability and performance observed compared to cheaper options.
    *   Users appreciate the security aspect of Fly GPUs, especially concerning data access compared to marketplace alternatives.

*   **Price Concerns Regarding Fly GPUs** (<https://news.ycombinator.com/item?id=43054331>, <https://news.ycombinator.com/item?id=43054146>, <https://news.ycombinator.com/item?id=43054184>, <https://news.ycombinator.com/item?id=43054456>, <https://news.ycombinator.com/item?id=43055431>)
    *   Fly.io's GPU offering is considered too expensive, especially for hobby use, simple inference, and projects that are not yet monetized.
    *   The monthly cost of "a GPU" at $1k is seen as unjustifiable for many users and use cases.
    *   Users are looking for more economical solutions, potentially suggesting the need for cheaper options like GPU slices or short-duration reservations.
    *   For some, the cost of renting Fly GPUs for a short period is comparable to buying a dedicated GPU server, making renting less attractive for continuous use.

*   **Developers Prefer LLMs and APIs over Raw GPUs** (<https://news.ycombinator.com/item?id=43054389>, <https://news.ycombinator.com/item?id=43054686>, <https://news.ycombinator.com/item?id=43054771>, <https://news.ycombinator.com/item?id=43054425>)
    *   Many developers, especially those using platforms like Fly.io and Cloudflare Workers, want PaaS-like solutions and managed infrastructure, not raw GPUs.
    *   These developers are more interested in using LLMs and AI models through APIs rather than managing GPU instances directly.
    *   The focus has shifted from building on raw infrastructure to leveraging managed services for AI functionalities.
    *   There's a potential market for data science and statistical modeling workloads that benefit from GPUs but are not necessarily LLMs, although Fly.io's customer base may not heavily represent this segment.
    *   Some executives are more interested in integrating ChatGPT-like LLMs into products than in traditional machine learning applications that already use AI.

*   **Technical Challenges and Limitations with Fly GPUs** (<https://news.ycombinator.com/item?id=43054074>)
    *   Users have encountered technical difficulties setting up LLMs on Fly.io GPU machines due to infrastructure limitations.
    *   Issues include poor support for streaming responses, which is crucial for LLM experiences.
    *   Challenges exist in deploying large LLM models as Docker images, with no easy way to handle large model files efficiently, leading to complex workarounds and potential performance issues when scaling.

*   **Suggestions for Fly.io to Offer LLM APIs and Managed Services** (<https://news.ycombinator.com/item?id=43054686>, <https://news.ycombinator.com/item?id=43054337>)
    *   Given Fly.io's existing GPU infrastructure, it is suggested they should consider offering managed LLM APIs or a "Workers AI" like service, similar to Cloudflare.
    *   This would align better with the needs of their target developers who prefer PaaS solutions and easy access to AI functionalities.
    *   Offering APIs for various models could be more appealing to developers who find model dockerization and self-hosting burdensome.

*   **Critique of GPU Cloud Pricing and Market Dynamics** (<https://news.ycombinator.com/item?id=43054293>, <https://news.ycombinator.com/item?id=43055023>, <https://news.ycombinator.com/item?id=43054641>, <https://news.ycombinator.com/item?id=43054935>, <https://news.ycombinator.com/item?id=43054486>, <https://news.ycombinator.com/item?id=43054345>)
    *   The price of inference compute, primarily GPUs, has significantly decreased, making managed APIs more competitive.
    *   Concerns are raised that Fly.io's GPU offering might not be competitively priced compared to other cloud providers or industry trends.
    *   Some argue that Fly.io might be overemphasizing security concerns with GPUs, especially if the market doesn't prioritize it, and should focus on price competitiveness instead.
    *   There's a discussion about the limited market for partial GPUs (MIG) in the cloud, suggesting users typically want full GPUs or managed solutions.
    *   Comparisons are made to self-hosting GPU hardware versus renting, with some arguing that owning hardware can be more cost-effective in certain scenarios, while others highlight the benefits of renting from specialized GPU clouds like Voltage Park in terms of cost and scalability.

*   **Appreciation for Fly.io's Openness and Honesty** (<https://news.ycombinator.com/item?id=43054033>, <https://news.ycombinator.com/item?id=43054924>, <https://news.ycombinator.com/item?id=43054144>)
    *   The blog post is praised for its honesty, openness, and willingness to admit being wrong.
    *   Fly.io is respected for being public about their experiences and learnings, which is seen as valuable and commendable.
    *   The quality of the blog post and its interlinking with other articles on the blog is appreciated.

*   **Questions About Fly.io's Future GPU Plans and Strategy** (<https://news.ycombinator.com/item?id=43054061>, <https://news.ycombinator.com/item?id=43054291>, <https://news.ycombinator.com/item?id=43054935>)
    *   Questions are raised about which specific GPU services Fly.io will continue to offer.
    *   There's curiosity about Fly.io's runway and financial stability, especially in light of scaling back GPU ambitions.
    *   Some commenters wonder about Fly.io's overall value proposition if low-cost GPUs are not a focus, questioning what differentiates them from larger cloud vendors.

*   **Technical Discussions on GPUs, Hardware, and Virtualization** (<https://news.ycombinator.com/item?id=43054292>, <https://news.ycombinator.com/item?id=43054118>, <https://news.ycombinator.com/item?id=43054733>, <https://news.ycombinator.com/item?id=43054345>, <https://news.ycombinator.com/item?id=43054486>, <https://news.ycombinator.com/item?id=43054998>)
    *   Discussions revolve around the challenges of GPU virtualization, particularly the desire for secure and isolated GPU slicing for VMs, similar to CPU, RAM, and network virtualization.
    *   Concerns are raised about the durable value of GPU hardware as assets, considering rapid depreciation due to energy efficiency and technological advancements.
    *   Nvidia is criticized for deliberately making GPU virtualization and driver support difficult, creating opportunities for competitors like Intel and AMD.
    *   The limitations of PCIe passthrough for GPU virtualization are mentioned, especially in the context of AMD GPUs, and the potential for future improvements with ROCm.
    *   Commenters discuss the end of Moore's Law and the increasing focus on parallel computing, with GPUs being well-suited for parallel workloads like LLMs, but questions remain about other potential uses for massive parallel computing power beyond AI.
    *   Detailed technical points are made about GPU usage for different model sizes and input types, suggesting that CPUs are still viable and often more cost-effective for many inference tasks, and that GPUs might not be the optimal abstraction for extremely large models.