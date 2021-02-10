doc_type = {
    "{案卷（首页）": "DocNewajsy",
    "现场检查方案": "DocNewCheckPlan",
    "现场检查记录": "DocCheckResult",
    "现场处理措施决定书": "DocLocalDeal",
    "询问通知书": "DocNewInquiryNotice",
    "责令限期整改指令书": "DocCorrect",
    "立案审批表": "DocRegistCaseAudit",
    "行政强制审批表": "DocNewXzqzspb",
    "查封扣押决定书": "DocNewCfkyjds",

    "延长查封扣押期限决定书": "DocNewYccfkyqxjds",
    "查封扣押处理决定书": "DocNewCfkycljds",
    "整改复查意见书": "DocOpinion",
    "案件处理呈批表": "DocNewTzgdjds",
    "行政处罚集体讨论记录": "DocNewXzcfjttljl",
    "案件移送审批表": "DocNewTransferApproval",
    "案件移送书": "DocNewTransfer",
    "行政处罚告知书": "DocNewXzcfgzs",
    "行政处罚听证告知书": "DocNewXzcftzgzs",
    "行政处罚听证会通知书": "DocNewXzcftzhtzs",
    "案件延期审批表": "DocNewajyqspb",
    "行政处罚决定书（单位）": "DocNewXzcfjds_fdc",
    "文书送达回执": "DocNewServiceReceipt",
    "结案审批表": "DocNewjaspb",
}


def name(wszl, docName):
    lowerDocname = docName[0].lower() + docName[1:]
    return " ".join(
        [
            "/**" + wszl + "*/",
            "if (doc.getWszl().equals(DocEnum.",
            docName,
            ".getName())) {",

            docName,
            lowerDocname,
            "= ",
            lowerDocname + "Service.findByGuid(docGuid);",
            lowerDocname + ".setWsbh(newWsbh);",
            lowerDocname + "Service.save(",
            lowerDocname,
            ");",
            "return \"成功\";}"
        ])

def service(docName):
    return " ".join(
        [
            "@Autowired",
            "private ",
            docName + "Service " + docName[0].lower() + docName[1:] + "Service;"])
for wszl, docName in doc_type.items():
    print(name(wszl, docName))

for wszl, docName in doc_type.items():
    print(service(docName))

