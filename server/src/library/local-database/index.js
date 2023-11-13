// import * as graph from './graph.json';
// import * as indexBook from './indexBook.json';
// import * as products from './products.json';
// import * as reviews from './reviews.json';
// import * as insights from './insights.json';
// import * as features from './features.json';
// import * as users from './users.json';
// export const DEFAULT_PRODUCT_IMAGE =
//   'https://res.cloudinary.com/diijxiitu/image/upload/v1693319158/2023-08-29_21-25-02_vxr2xs.png';
// export const findManyProductByIds = (ids) => {
//   const setIds = new Set(ids);
//   return products.filter((product) => setIds.has(product.id));
// };
// export const getProducts = ({ page, pageSize, sort, q }) => {
//   const filteredProducts = products.filter((product) => {
//     const productNameEn = product?.product_name || '';
//     const productNameJa = product?.translations?.product_name['ja'] || '';
//     return productNameEn.includes(q) || productNameJa.includes(q);
//   });
//   return filteredProducts;
// };
// export const generateDataInsight = (mainCategory, report) => {
//   let totalReviews = 0;
//   const insight = [];
//   for (const key in report.dataInsight) {
//     const values = key.split('/');
//     const category = values[0];
//     if (category !== mainCategory) continue;
//     const subCategory = values[1];
//     const numberReviews = report.dataInsight[key].length;
//     totalReviews += numberReviews;
//     const keywords = report.dataInsight[key].map((item) => item.keyword);
//     const uniKeywords = [...new Set(keywords)];
//     const content = subCategory;
//     insight.push({ content, reason: uniKeywords.join(), numberReviews });
//   }
//   const finalInsight = insight
//     .map((item) => {
//       return {
//         ...item,
//         percentageReviews: Math.round(
//           (item.numberReviews / totalReviews) * 100,
//         ),
//       };
//     })
//     .sort((a, b) => b.numberReviews - a.numberReviews)
//     .map((item, id) => {
//       return { id, ...item };
//     });
//   return finalInsight;
// };
// export const generateDataInsightV2 = (mainCategory, productIds) => {
//   // console.log({ mainCategory, productIds });
//   const setOfProductIds = new Set(productIds);
//   const filteredInsights = insights.filter((insight) => {
//     return (
//       setOfProductIds.has(insight.productId) &&
//       mainCategory === insight.mainCategory
//     );
//   });
//   const mapOfInsights = new Map();
//   const setOfReviewIds = new Set();
//   for (let insight of filteredInsights) {
//     const { keyword, reviewId } = insight;
//     setOfReviewIds.add(reviewId);
//     if (!mapOfInsights.has(keyword)) {
//       mapOfInsights.set(keyword, []);
//     }
//     const values = mapOfInsights.get(keyword);
//     values.push(insight);
//     mapOfInsights.set(keyword, values);
//   }
//   const entries = Array.from(mapOfInsights.entries());
//   entries.sort((a, b) => {
//     const aReviews = a[1].length;
//     const bReviews = b[1].length;
//     return bReviews - aReviews;
//   });
//   // console.log('setOfReviewIds size', setOfReviewIds.size);
//   const totalReviews = setOfReviewIds.size;
//   const customData = entries.map((item, id) => {
//     const [keyword, insights] = item;
//     const numberReviews = insights.length;
//     const percentageReviews = Math.round((numberReviews / totalReviews) * 100);
//     return {
//       id,
//       tag: keyword,
//       content: keyword,
//       reason: insights.map((item) => item.content).join('\n'),
//       numberReviews,
//       percentageReviews,
//     };
//   });
//   return customData.length > 5 ? customData.slice(0, 5) : customData;
//   // return filteredInsights;
// };
// export const generateCustomerProfileReport = (mainCategory, report) => {
//   const hashMap = {};
//   for (const key in report.dataInsight) {
//     const values = key.split('/');
//     const category = values[0];
//     if (category !== mainCategory) continue;
//     const subCategory = values[1];
//     if (!hashMap[subCategory]) {
//       hashMap[subCategory] = {
//         highRatings: 0,
//         lowRatings: 0,
//       };
//     }
//     const reviews = report.dataInsight[key];
//     for (const review of reviews) {
//       if (review.star >= 3) {
//         hashMap[subCategory].highRatings += 1;
//         continue;
//       }
//       hashMap[subCategory].lowRatings += 1;
//     }
//   }
//   const insights = [];
//   let index = 0;
//   for (const category in hashMap) {
//     const { highRatings, lowRatings } = hashMap[category];
//     const allRatings = highRatings + lowRatings;
//     const insight = {
//       id: index,
//       keyword: category,
//       allRatings,
//       highRatings,
//       lowRatings,
//     };
//     insights.push(insight);
//     index += 1;
//   }
//   return insights;
// };
// export const generateCustomerProfileReportV2 = (mainCategory, productIds) => {
//   const setOfProductIds = new Set(productIds);
//   const filteredInsights = insights.filter((insight) => {
//     return (
//       setOfProductIds.has(insight.productId) &&
//       mainCategory === insight.mainCategory
//     );
//   });
//   const mapOfInsights = new Map();
//   for (let insight of filteredInsights) {
//     const { keyword } = insight;
//     if (!mapOfInsights.has(keyword)) {
//       mapOfInsights.set(keyword, []);
//     }
//     const values = mapOfInsights.get(keyword);
//     values.push(insight);
//     mapOfInsights.set(keyword, values);
//   }
//   const entries = Array.from(mapOfInsights.entries());
//   entries.sort((a, b) => {
//     const aReviews = a[1].length;
//     const bReviews = b[1].length;
//     return bReviews - aReviews;
//   });
//   // console.log({ entries });
//   const customData = entries.map((item, id) => {
//     const [keyword, insights] = item;
//     const allRatings = insights.length;
//     const { highRatings, lowRatings } = insights.reduce(
//       (acc, curr) => {
//         if (curr.star >= 3) acc.highRatings += 1;
//         else acc.lowRatings += 1;
//         return acc;
//       },
//       { highRatings: 0, lowRatings: 0 },
//     );
//     return {
//       id,
//       tag: keyword,
//       keyword,
//       highRatings,
//       lowRatings,
//       allRatings,
//     };
//   });
//   // customData.length = 5;
//   return customData;
// };
// export const generateInsightReport = (productIds) => {
//   const setOfProductIds = new Set(productIds);
//   const filteredReviews = reviews.filter((review) => {
//     const { product_id } = review;
//     return setOfProductIds.has(product_id);
//   });
//   const numberOfReviewsAnalyzed = filteredReviews.length;
//   const setOfReviewsId = new Set(filteredReviews.map((review) => review.id));
//   const shortIndexBook = {};
//   for (const keyword in indexBook) {
//     const reviews = indexBook[keyword];
//     const filteredReviews = reviews.filter((review) => {
//       const { id } = review;
//       return setOfReviewsId.has(id);
//     });
//     if (filteredReviews.length > 0) {
//       shortIndexBook[keyword] = filteredReviews;
//     }
//   }
//   const shortGraph = {};
//   for (const category in graph) {
//     if (category === 'root') continue;
//     const keywords = graph[category];
//     for (const keyword of keywords) {
//       if (!shortIndexBook[keyword]?.length) continue;
//       if (!shortGraph[category]) {
//         shortGraph[category] = [];
//       }
//       const reviews = shortIndexBook[keyword].map((review) => {
//         const { id, star } = review;
//         return { id, star, keyword };
//       });
//       shortGraph[category].push(...reviews);
//     }
//   }
//   return { numberOfReviewsAnalyzed, dataInsight: shortGraph };
// };
// export const filterReviewsByProductsTagsAndCategory = (
//   productIds: string[],
//   tags: string[],
//   mainCategory: string,
// ) => {
//   const setOfProductIds = new Set(productIds);
//   const setOfTags = new Set(tags);
//   const filteredReviews = insights.filter((insight) => {
//     if (setOfTags.size > 0 && !setOfTags.has(insight?.keyword)) return false;
//     if (mainCategory && insight?.mainCategory !== mainCategory) return false;
//     if (setOfProductIds.size > 0 && !setOfProductIds.has(insight?.productId))
//       return false;
//     return true;
//   });
//   return filteredReviews;
// };
// export const filterReviewsByIds = (reviewIds: string[]) => {
//   const setOfReviewIds = new Set(reviewIds);
//   const filteredReviews = insights.filter((insight) => {
//     return setOfReviewIds.has(insight?.reviewId);
//   });
//   return filteredReviews;
// };
// export const getPermissions = (plan: string) => {
//   console.log({ plan });
//   const permissions = {};
//   for (const feature of features) {
//     const { featureName } = feature;
//     permissions[featureName] = feature[plan] === 'TRUE';
//   }
//   return permissions;
// };
// export const getUser = ({ email, password }) => {
//   const existingUser = users.find((user) => {
//     return user.email === email && user.password === password;
//   });
//   return existingUser;
// };
