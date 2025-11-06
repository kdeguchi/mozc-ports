PORTNAME=	bazel
DISTVERSION=	8.4.2
CATEGORIES=	devel java
MASTER_SITES=	https://github.com/bazelbuild/${PORTNAME}/releases/download/${DISTVERSION}/
PKGNAMESUFFIX=	8
DISTNAME=	bazel-${DISTVERSION}-dist

# TODO remove after these commits land in a release
PATCH_SITES=	https://github.com/bazelbuild/bazel/commit/
PATCHFILES=	a55aca5.patch:-p1 \
		00f76ea.patch:-p1

MAINTAINER=	vishwin@FreeBSD.org
COMMENT=	Fast and correct build system
WWW=		https://bazel.build/

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

NOT_FOR_ARCHS=	i386

BUILD_DEPENDS=	bash:shells/bash \
		zip:archivers/zip

USES=		cpe compiler:c++17-lang java python:3.9+ shebangfix zip
CPE_VENDOR=	google
JAVA_VERSION=	21
JAVA_VENDOR=	openjdk

SHEBANG_REGEX=	.*(sh|txt|_stub|stub_.*|bazel|get_workspace_status|protobuf_support|_so)

CONFLICTS_INSTALL=	bazel[0-9]*

BINARY_ALIAS=		python3=${PYTHON_CMD}

# The bazel binary is also a zip archive (extracted by the elf part), it must not be stripped
STRIP=

NO_WRKSUBDIR=	YES

MAKE_ENV+=	BAZEL_SH=${LOCALBASE}/bin/bash \
		JAVA_HOME=${JAVA_HOME} \
		JAVA_VERSION=${JAVA_VERSION} \
		TMPDIR=${WRKDIR}/bazel_tmp \
		EMBED_LABEL='${PORTVERSION}' \
		PATH=${LOCALBASE}/bin:$$PATH \
		SOURCE_DATE_EPOCH=$${SOURCE_DATE_EPOCH} \
		BAZEL_JAVAC_OPTS=${BAZEL_JAVAC_OPTS} \
		EXTRA_BAZEL_ARGS='--tool_java_runtime_version=local_jdk --java_language_version=${JAVA_VERSION} --tool_java_language_version=${JAVA_VERSION} --linkopt=-lm --host_linkopt=-lm'

.include <bsd.port.pre.mk>

.if ${ARCH} == "aarch64"
BAZEL_JAVAC_OPTS+=	"-J-Xmx1g -J-Xms128m"
.endif

# Have the location of the system-wide rc file reside ${ETCDIR}.
post-patch:
	@${REINPLACE_CMD} -e "s|/etc/bazel.bazelrc|${ETCDIR}/bazel.bazelrc|" \
		${WRKSRC}/src/main/cpp/BUILD
	@${REINPLACE_CMD} -e 's|%%JAVA_HOME%%|${JAVA_HOME}|' \
		${WRKSRC}/src/main/cpp/blaze_util_bsd.cc

do-build:
	${MKDIR} ${WRKDIR}/bazel_tmp
	(if [ -z "$${SOURCE_DATE_EPOCH}" ] ; \
	  then SOURCE_DATE_EPOCH=`grep TIMESTAMP ${DISTINFO_FILE} \
	    | ${SED} -e 's/[^0-9]//g'`; \
	fi ; \
	cd ${WRKSRC} && ${SETENV} ${MAKE_ENV} PATH=${BINARY_LINKDIR}:${PATH} ./compile.sh)

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/output/bazel ${STAGEDIR}${PREFIX}/bin
	@${MKDIR} ${STAGEDIR}${ETCDIR}
	${INSTALL_DATA} ${WRKSRC}/scripts/packages/bazel.bazelrc ${STAGEDIR}${ETCDIR}/bazel.bazelrc.sample

.include <bsd.port.post.mk>
