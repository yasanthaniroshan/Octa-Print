import fs from 'fs/promises';

export const actions = {
	upload: async ({ request }) => {
		const data = Object.fromEntries(await request.formData());
		const filePath = "src/files/uploaded/"+ data.pdf_file.name;
		fs.writeFile(filePath, new Uint8Array(data.pdf_file));

		return {
			status: 200,
			body: {
				message: 'File uploaded successfully'
			}
		};
	}
};
