from datetime import datetime
from crewai import Task

class biology_crew_tasks():
    def creating_task_task(self, agent):
        return Task(
            description=""" Identifying the information that a user wants to find out and delegate it to
             the corresponding agent and task """,
            agent=agent,
            async_execution=True,
            expected_output=""" A description of a task that the other agent should do.
            For example "It looks like the user asked about genetic question.
            Senior geneticist agent, you should answer what APOE gene is and
            provide information about it that the user asked about"""
        )
    
    def fetch_genetic_info_task(self, agent, context):
        return Task(
            description="""Extract of key information that user asked about genetics that you
            summarize and bring the essential information to the user. Always provde links for sources as well""",
            agent=agent,
            context=context,
            async_execution=True,
            expected_output=""" The MTOR gene, known as the mechanistic target of rapamycin,
            plays a significant role in cellular responses to stresses such as DNA damage
            and nutrient deprivation. This protein acts as the target for the cell-cycle
            arrest and immunosuppressive effects of the FKBP12-rapamycin complex. Studies
            have investigated the association of genetic variations within the MTOR pathway
            with longevity, but the results are varied and often non-significant after
            adjusting for multiple hypothesis testing.
            One study examined 1,018 SNPs within a 10-kb window around 40 MTOR signaling genes
            in 417 nonagenarian participants compared to 476 younger controls.
            This study found a significant association of genetic variation in
            the MTOR pathway with familial longevity in a Dutch population, although
            no individual gene showed significant association after correcting
            for multiple testing. Other studies involving different populations,
            including Americans of Japanese origin and Southern Italians,
            tested numerous tagSNPs within key MTOR complex genes
            (MTOR, RPTOR, and RICTOR, as well as RPS6KA1) for associations
            with longevity and health span phenotypes. These studies did not
            find significant associations between genotypes and longevity or
            aging-related biological, clinical, or functional phenotypes after
            multiple test correction.
            In terms of diseases, MTOR pathway dysregulation is implicated
            in various conditions, including AIDS-Associated Nephropathy, various
            forms of cancer, and neurological and psychiatric disorders, indicating
            its complex role in human health and disease.
            For more detailed information, please visit the NCBI MTOR
            gene page(here is the link to the page).
            """
        )


